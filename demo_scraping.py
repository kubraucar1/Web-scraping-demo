from csv import writer

import requests
from bs4 import BeautifulSoup

url= 'https://www.sadikturan.com/'
response = requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
courses = soup.find_all(class_='kurs')

with open('courses.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['pic','title','explanation','udemy_link','site_link'])



    for course in courses:
        courses_pic= course.find('img')['src']
        courses_title= course.find(class_='media-body').find('h2').string
        courses_explanation= course.find(class_ ='media-body').find('span').string
        links=course.find(class_='card-footer').find_all('div')[1].find_all('a')
        courses_udemy_link = links[0]['href']
        courses_site_link =url + links[1]['href']
        
        csv_writer.writerow([courses_pic,courses_title,courses_explanation,courses_udemy_link,courses_site_link])
