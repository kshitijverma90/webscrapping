import bs4, requests
import pandas as pd
getPage = requests.get('https://mausam.imd.gov.in/bengaluru/')
weather = bs4.BeautifulSoup(getPage.text, 'html.parser')
print(weather)
capitals=weather.find_all(class_='capital')
# print(capitals)
capitalname=[capital.find('h3').get_text() for capital in capitals]
temperaturenow=[capital.find(class_='val').get_text() for capital in capitals]
wind=[capital.find(class_='wind').get_text() for capital in capitals]
weather=pd.DataFrame(
    {
        'city':capitalname,
        'temperature':temperaturenow,
         'wind':wind,
    }
)
weather.to_csv('weather.csv')