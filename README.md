# Takehome_assignmet

<a href="https://github.com/claire56">
    <img alt="screen shot" src="Screen Shot 2019-05-22 at 10.24.02 AM.png" width="900" height="500">
    </a>


## Table of Contents
* [Overview](#Overview)
* [Fetch the historical prices and dates](#Fetch-the-historical-prices-and-dates)
* [Database[(#Database)
* [Commodity endpoint](#Commodity-endpoint)
* [unittest](#unittest)
* [Tech Stack](#Tech-Stack)
* [Setup and installation](#Setup-and-installation)
* [Demo](#Demo)
* [Future Features](#Future-Features)
* [Detailed question](#Detailed-questions)


### Fetch the historical prices and dates
i used the python requests module to get html from the urls, and beautiful soup to extract the required data 


### Database
I stored the data in a PostgreSql  database, details about the seeding can be found in the <a href="href="https://github.com/claire56/seed.py">seed.py </a>

#### Database putput screenshot
<a href="https://github.com/claire56">
    <img alt="screen shot" src="Screen Shot 2019-05-22 at 10.32.54 AM.png" width="900" height="500">
    </a>

Please use Python (ver 3) to complete the test assessment.
1. Please write a program to fetch the historical prices and dates of gold and silver from these 2 URLs:
https://www.investing.com/commodities/gold-historical-data
https://www.investing.com/commodities/silver-historical-data
 
and store them locally (in a csv file, or other file or database, as you see fit). 
Please extract the Date and Price fields only from the current static page.

2. Please write a second program that will start an API web-service on port 8080 (use flask) that will return the stored data
Create an endpoint that will accept HTTP GET with following arguments, and returning a json time series, mean and variance computed over the specified period
  * start_date - required (iso format like 2017-05-10)
  * end_date - required (iso format like 2017-05-22)
  * commodity_type - required (gold, silver)
  
example of calling by using curl:
  curl 'http://127.0.0.1:8080/commodity?start_date=2017-05-10&end_date=2017-05-22&commodity_type=gold'

3. Bonuses
- Using docker/docker compose to wrap the application in containers is a plus.
- Using mysql database to store data is a plus (order of preference: mysql, postgres, sqlite, csv).
- Writing unit test cases is a plus.

example of output data:
  {
  "data": {
 "2017-05-10": 1253.06,
 "2017-05-11": 1280.46,
 "2017-05-12": 1278.21
  }
  "mean": 1270.57,
  "variance": 231.39
  }




