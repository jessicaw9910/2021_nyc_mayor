#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

## import candidate names copied from election website
my_file = open("names.txt", "r")
names = my_file.readlines()
names = [i.replace('\n', '') for i in names]

## input url and number of rounds
url_base = input('Enter current URL with the terminal round number removed: ')

no_rounds = int(input('Enter number of rounds reported: '))
rounds = [i for i in range(1, no_rounds + 1)]

## create urls for all rounds
url_total = []
for n in rounds:
    url_total.append(url_base + str(n) + ".html")

## extract the table data for each round
rounds_total = []
for url in url_total:
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
        
    soup = BeautifulSoup(page.content, "html.parser")
        
    data = []

    tables = soup.findChildren('table')
    tables[0]

    rows = tables[0].findChildren('td')

    for row in rows:
        cells = row.findChildren(['td'])
        for cell in cells:
            value = str(cell.string)
            data.append(value.lstrip())
    rounds_total.append(data)

## extract the results per candidate per round
rounds_list = []

for name in names:
    round_list = []
    for i in rounds:
        temp = rounds_total[i-1][rounds_total[i-1].index(name) + 1]
        round_list.append(temp)
    rounds_list.append(round_list)
    
rounds_list = [list(map(lambda x:x.split(' ')[0], group)) for group in rounds_list]

## create dataframe from list of lists
df_output = pd.DataFrame(rounds_list, 
                         columns = ["Round " + str(i) for i in rounds])
df_output.index = names

## output dataframe to CSV
cwd = os.getcwd()
path = cwd + "/output.csv"
df_output.to_csv(path)