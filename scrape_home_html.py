from bs4 import BeautifulSoup

# Open and read the html file
with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    # Create a BeautifulSoup object, using the 'lxml' parser 
    soup = BeautifulSoup(content, 'lxml')

    # 1. Get the list of courses
    # Find the specified tags
    courses_html_tags = soup.find_all('h5')
    
    print("Available courses:")
    for i, course in enumerate(courses_html_tags):
        print(i+1, course.text)

    print()
    
    # 2. Get the prices of courses
    # Retrieve the div tags with class='div'
    course_card = soup.find_all('div', class_='card')

    for course in course_card:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')
