from sqlalchemy import func
from data_model import Silver ,Gold
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
from datetime import datetime , date

from data_model import connect_to_db, db
from server import app


def load_silver():
    """Load gold metals into database."""

    print("silver_metals")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Silver.query.delete()

    # Get the data from url

    silver= requests.get('https://www.investing.com/commodities/silver-historical-data')
    # create beautiful soup object
    silver_soup =BeautifulSoup(silver.content , 'html.parser' )
    # find the desired table
    silver_table=silver_soup.find(id='curr_table')
    # get desired data from table children
    silver_data = list(silver_table.children)[3]
    # find the rows
    rows = silver_data.find_all('tr')
    # get row text
    rows = [row.get_text() for row in rows]
    # split each row on new line
    row_split = [row.split('\n') for row in rows] 

    for row in row_split:
        date = row[1].replace(',','') #replce comma with nothing
        d = pd.to_datetime(date) #change string to datetime
        date = d.date() #get only the date
        price= float(row[2]) #change price to float from string


        silver = Silver(date=date, price=price)

        db.session.add(silver)
        db.session.commit()
    
    db.session.commit()


def load_gold():
    """Load gold metals into database."""

    print("gold_metals")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Gold.query.delete()

    # Get the data from url

    gold= requests.get('https://www.investing.com/commodities/gold-historical-data')
    # create beautiful soup object
    gold_soup =BeautifulSoup(gold.content , 'html.parser' )
    # find the desired table
    gold_table=gold_soup.find(id='curr_table')
    # get desired data from table children
    gold_data = list(gold_table.children)[3]
    # find the rows
    rows = gold_data.find_all('tr')
    # get row text
    rows = [row.get_text() for row in rows]
    # split each row on new line
    row_split = [row.split('\n') for row in rows] 

    for row in row_split:
        date = row[1].replace(',','') #replce comma with nothing
        d = pd.to_datetime(date) #change string to datetime
        date = d.date() #get only the date
        price= float(row[2].replace(',','')) #change price to float from string


        gold = Gold(date=date, price=price)

        db.session.add(gold)
        db.session.commit()
    
    db.session.commit()





if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_gold()
    load_silver()
    # set_val_user_id()

