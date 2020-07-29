import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#Route of bolsa de madrid WEB
url_page = 'https://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'

page = requests.get(url_page).text
soup = BeautifulSoup(page, features='html.parser')

table = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})


# iterating by the name of the extract and the last price of the summary
name=""
last_price=""
number_row=0
for row in table.find_all("tr"):
    if number_row==1:
        number_cell=0
        for cell in row.find_all('td'):
            if number_cell==0:
                name=cell.text
                print("Indice:", name)
            if number_cell==2:
                last_price=cell.text
                print("Valor:", last_price)
            number_cell=number_cell+1
    number_row=number_row+1


# Creating CSV file for store
with open('bolsa_madrid_IBEX35.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, last_price, datetime.now()])