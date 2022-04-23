from urllib import request
import pandas as pd
import bs4,requests

getpage=requests.get('https://www.timeanddate.com/weather/india/bengaluru/ext')
item=bs4.BeautifulSoup(getpage.text,'html.parser')
#print(item)
# cloudy=item.find_all('div')
# temperaturenow=[cloud.find_all(class_='weather-graph') for cloud in cloudy]
# print(temperaturenow)
lines=item.find('li').get_text()
links=item.find('a').get_text()
#print(lines)
print(links)