# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:59:45 2020

@author: joamat
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html'
req = requests.get(url)
if req.status_code == 200:
    print('Status code: 200')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')

table = soup.find('div', {'class': 'articletable'})
table_str = str(table)
df = pd.read_html(table_str)[0]
print(df)

#table_price = soup.find('table', {'class': 'articletable'}).find('td').find('span')
#table_price_str = str(table_price)
#df_price = pd.read_html(table_price_str)[0]
##df_price_last = df_price.iloc[:,-1]
#print(df_price)



#df.to_csv('./graphicscards-benchmarked-and-ranked.csv')