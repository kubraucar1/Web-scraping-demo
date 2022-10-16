
from csv import writer

import requests
from bs4 import BeautifulSoup

search_input = input('search something: ').replace(' ','+')
link= "https://www.google.com/search?q="+ search_input

header_params= {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.42"}

response = requests.get(link,headers =header_params)
soup = BeautifulSoup(response.content,"html.parser")

result =soup.find_all('div',class_='MjjYud')

with open('google_search.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['site'])
    
for div in result:
    site_links = div.find('a')['href']
   
    csv_writer.writerow([site_links])