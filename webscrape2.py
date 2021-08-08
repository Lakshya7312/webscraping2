import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
tables = soup.find_all('table')

names = []
distances = []
masses = []
radii = []

rows = tables[7].find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        name = cells[1].text
        names.append(name[:-1])

        distance = cells[5].text
        distances.append(distance[:-1])

        mass = cells[7].text
        masses.append(mass[:-1])

        radius = cells[8].text
        radii.append(radius[:-1])

dict = {'Constellation': names, 'Distance': distances, 'Mass': masses, 'Radius': radii} 

df = pd.DataFrame(dict)
  
df.to_csv('webscrape2result.csv')
print("Process Completed")