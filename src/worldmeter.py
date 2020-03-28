import requests
import bs4
from datetime import date, timedelta
import json
from CountryData import CountryData


def parse_data(data):
    data=data.replace(' ','').replace(u"\u00A0",'').replace('+','').replace(',','')
    if(data==''):
        return 0
    return int(data)

today=date.today()-timedelta(days=1)
print(today)
page=requests.get("https://www.worldometers.info/coronavirus/")

soup=bs4.BeautifulSoup(page.content,'html.parser')
yesterday_data=soup.find('div',{'id':'nav-yesterday'})
results=yesterday_data.find_all('tr')
print(len(results))
country_dictionery={}
count=0
f=open('../resources/{}.json'.format(today),'w')

for i in range(1,len(results)):
    try:
        count=count+1
        country_attributes=results[i].find_all('td')
        country=country_attributes.pop(0).text
        total_cases=parse_data(country_attributes.pop(0).text)
        new_cases=parse_data(country_attributes.pop(0).text)
        total_deaths=parse_data(country_attributes.pop(0).text)
        new_deaths=parse_data(country_attributes.pop(0).text)
        total_recovered=parse_data(country_attributes.pop(0).text)
        country_dictionery[country]=CountryData(country,total_cases,new_cases,total_deaths,new_deaths,total_recovered,count).serialize()
    except IndexError as e:
        print(e)

json.dump(country_dictionery,f)
