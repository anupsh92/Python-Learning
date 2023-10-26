import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Replace 'url_of_the_website' with the actual URL of the webpage containing the table
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser').find_all("table")[1].tbody
rows = soup.find_all('tr')
columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]
df = pd.DataFrame(columns=columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    if len(tds) == 6:
        values = [tds[0].text, tds[1].text, '', tds [2].text, tds [3].text]
    else:
        values = [td.text for td in tds]


    df = df._append(pd.Series(values, index=columns),ignore_index=True)
    print(df)
    #df.to_csv(r'C:\Users\Senpiper\Documents\GitHub\Python-Learning'+'\\countries.csv',index=False)








