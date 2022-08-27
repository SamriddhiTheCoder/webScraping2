import time
import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
star_data = []

def scrape():  
    page = requests.get(START_URL)
    soup = BeautifulSoup(page.content,"html.parser") 
    temp_list = []
    time.sleep(3)
    table_tag = soup.find_all("table")
    tr_tag = table_tag[7].find_all("tr")
    for tr in tr_tag:
        td = tr.find_all("td")
        row = [i.text.rstrip()for i in td]
        temp_list.append(row)

    star_names = []
    distances  = []
    masses = [] 
    radiuses = []
    for i in range(1, len(temp_list)):
        star_names.append(temp_list[i][0])
    for i in range(1, len(temp_list)):
        distances.append(temp_list[i][5])
    for i in range(1, len(temp_list)):
        masses.append(temp_list[i][7])
    for i in range(1, len(temp_list)):
        radiuses.append(temp_list[i][8])

    df = pd.DataFrame(star_data)
    df.insert(0, 'Name', star_names)  
    df.insert(1, 'Distance', distances)  
    df.insert(2, 'Mass', masses) 
    df.insert(3, 'Radius', radiuses) 
    df.to_csv("data.csv")

scrape()