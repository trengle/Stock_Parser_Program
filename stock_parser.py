#! python3
import os
# import shutil
import csv

import logging
from datetime import datetime
# import pprint

"""
This program assumes that user creates a folder called "Stock_Parser" on Desktop,
and that the stocks.csv in located in that folder. 
"""

#create a log file on startup.  
#Anytime the program is run it should use the same log file to write to. 
#NEVER EVER log personal information. Put 'starting program, opening file, writing file, ALWAYS log INFO)

logging.basicConfig(
    filename="log.log",  # Log file name
    level=logging.INFO,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)

# You should print a line in it 'Starting Program...'
logging.info("Starting Program...")

DATE = datetime.now().strftime("%m-%d-%y")

# Scan the files the client sends you.  

#sets the default path to the user's Desktop
desktopPath=os.path.join(os.path.expanduser("~"),'Desktop')
#sets cwd to the Stock_Parser folder
workingDir=os.path.join(desktopPath,"Stock_Parser")
os.chdir(workingDir)

rowList=[]
with open("stocks.csv") as file:
# Scan each row.  
    reader = csv.reader(file)
    for id, name, symbol, price, sector, dividend, pe, date, bluechip in reader:
        rowList.append({"id":id, "name":name, "symbol":symbol, "price":price, "sector":sector, "dividend":dividend, "pe":pe, "date":date, "bluechip":bluechip})
# Find the sector.
for stock in rowList:
# Create a folder named after the sector.  
    os.chdir(workingDir)
    os.makedirs(rf'{stock['sector']}', exist_ok=True)
    # Create a .txt file for the stock name
    path = os.path.join(workingDir,stock['sector'])  
    os.chdir(path)
    # stock name that already exists then you can skip it.  
    if os.path.exists(f'{stock['name']}.txt'):
        continue
    else:
        with open(rf'{stock['name']}.txt', "w") as txtfile:
            #update the log file with a line 'Adding row for <Stock Name>'.
            logging.info(f'Adding row for {stock['name']}')
            # For each column of the stock add a row to the .txt file with the following information:
            # todays date in the following format 
            # MM-DD-YY, Share Price, Dividend, PE. $$ the first column is the ID, 2nd is stock name, 3rd column is stock symbol, 4th share price (needed), 5th column is the category, 6th column is the dividend, 7th is the PE, 8th column is next earnings date, final column is ...ignore for now, is it a blue chip stock.
            txtfile.write(rf'{DATE} {stock['price']} {stock['dividend']} {stock['pe']}')
            #After adding this update the log file with '<Stock Name> added!'.
            logging.info(f'{stock['name']} added!')
logging.info("Program Finished")