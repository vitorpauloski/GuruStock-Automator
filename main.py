import guru
import csv
import json
import time
from datetime import datetime
import os

home_directory = os.path.expanduser('~')
documents_directory = os.path.join(home_directory, 'Documents')
gurustock_automator_directory = os.path.join(documents_directory, 'GuruStock Automator')
gurustock_automator_settings = os.path.join(gurustock_automator_directory, 'settings.json')

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

with open(gurustock_automator_settings, 'r') as f:
    settings = json.load(f)

session = guru.Session(settings['token'])

def getData():
    input_list = []
    with open(settings['input_file'], 'r') as f:
        dictreader = csv.DictReader(f, delimiter = ';')
        for i in dictreader:
            input_list.append(i)

    tickers = []
    for i in input_list:
        tickers.append(i['ticker'])

    response = session.getMarketData(tickers)

    for i in response:
        i['update_time'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    with open(settings['output_file'], 'w') as f:
        fieldnames = ['ticker', 'name', 'close', 'price', 'variation_percent', 'update_time']
        dictwriter = csv.DictWriter(f, delimiter = ';', fieldnames = fieldnames)
        dictwriter.writeheader()
        for i in response:
            dictwriter.writerow(i)

while True:
    getData()
    clear_terminal()
    print('------------------------------')
    print(f"UPDATED at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print('------------------------------\n')
    j = settings['reload_time']
    while j > 0:
        print('Next update in ' + str(j) + ' second(s)     ', end = '\r', flush = True)
        time.sleep(1)
        j = j -1
    print('Updating...                       ', end = '\r', flush = True)
