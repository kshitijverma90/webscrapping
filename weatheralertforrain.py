import bs4, requests
import pandas as pd
getPage = requests.get('https://www.skymetweather.com/forecast/weather/india/karnataka/bangalore%20urban/bengaluru')
weather = bs4.BeautifulSoup(getPage.text, 'html.parser')
print(weather.prettify())

