#web-scrapper.py

#imports
from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame

#website
ffcResponse = requests.get('https://fantasyfootballcalculator.com/adp/ppr/12-team/all/2021')

#Beautiful soup
htmlSoup = Soup(ffcResponse.text,'html.parser')

#get the table
tables = htmlSoup.find_all('table')
print(tables)

adp_table = tables[0]

rows = adp_table.find_all('tr')

tableHead = rows[0]

first_data_row = rows[1]

print(first_data_row)


