from bs4 import BeautifulSoup
import requests
import time

def find_jobs(save_to_file=False):
    html_text = requests.get('https://www.brightnetwork.co.uk/graduate-jobs/technology/in-london/').text
    # To print html_text specify the encoding: print(html_text.encode('utf-8'))

    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup.encode('utf-8'))

    # Get the first match only
    jobs = soup.find_all('div', class_='tw-relative search-result-card tw-content-center tw-min-h-32 tw-border tw-border-solid tw-border-grey tw-rounded-[9px] tw-bg-white tw-my-4 tw-p-6')
    for index, job in enumerate(jobs):
        # Get the a tag from inside this div
        company_name = job.find('div', class_='tw-flex tw-flex-col tw-text-sm tw-content-center tw-gap-2 tw-justify-center').find('a')
        if company_name != None:
            company_name = company_name.text.replace(" ", "")

        # Get the skills
        salary = job.find('span', class_='tw-font-medium')
        if salary != None:
            salary = salary.text

        # Get the deadline 
        deadline = job.find_all('span')
        # Get the 1st element in 2nd position as the deadline is in the second span for most of the adverts
        if len(deadline) > 1:
            # Get the first position element
            deadline = deadline[1]
        else:
            deadline = deadline[0]
        
        # Get the text only
        if deadline != None:
            deadline = deadline.text

        # Get the link for the job post
        link = job.div.a['href']

        if link != None:
            link = link
        
        if save_to_file == True:
            with open(f'Posts/{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name}\n')
                f.write(f'Salary: {salary}\n')
                f.write(f'{deadline}\n')
                f.write(f'Link: https://www.brightnetwork.co.uk{link}\n')
            print(f'Post saved as {index}.txt')

        else:
            print(f'Company Name: {company_name}')
            print(f'Salary: {salary}')
            print(f'{deadline}')
            print(f'Link: https://www.brightnetwork.co.uk{link}\n')


if __name__ == "__main__":
    
    # Variable for mode selection
    mode_selected = False

    while True:
        if mode_selected == False:
            print("Hello, Scrape graduate tech job posts on bright network...")
            print("SELECT:\n1. Show result on screen\n2. Save result to a txt file")
            select = int(input("Your selection: "))
            if select == 1:
                save_to_file = False
            elif select == 2:
                save_to_file = True
            # Change mode to skip prompt for next iteration in 10 minutes
            mode_selected = True

        find_jobs(save_to_file)

        # Wait minutes
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)