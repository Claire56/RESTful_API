from flask import Flask ,render_template, session,jsonify, request ,redirect, make_response
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import numpy as np
# from sqlalchemy import func
import json
import os
import secrets
from flask import send_from_directory 
import pandas as pd 
import data_model as dm



app = Flask('__name__')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


app.secret_key = os.environ.get('key') 


from sqlalchemy import create_engine
engine = create_engine('postgresql:///goldsilver')
connection = engine.connect()


@app.route('/commodity')
def get_time_series():
	# get the values for urguments
	start_date = request.args.get('start_date')
	end_date = request.args.get('end_date')
	commodity_type = request.args.get('commodity_type')

	# determine what table to querry based on the commodity type
	if commodity_type == 'gold':
		table_name='gold_metals'

	elif commodity_type == 'silver':
		table_name ='silver_metals'

	# query the database and calculate mean and variance
	# my_query = "SELECT date,price FROM "+table_name+" WHERE date between '"+start_date+"'  and '"+end_date+"' ;"
	# results = connection.execute(my_query).fetchall()
	
        # changed below code to cater for sql injections

	
	my_query = "SELECT date,price FROM %table_name WHERE date between %start_date  and %end_date ;"
	results = connection.execute(my_query,(table_name,start_date,end_date)).fetchall()
	r = [dict(row) for row in results]
	dates = [str(ri['date']) for ri in r]
	prices = [float(ri['price'])for ri in r]
	d = dict(zip(dates, prices))
	data = d
	mean =round(sum(prices)/len(prices),2) 
	variance = round(np.var(prices),2)
	resp = make_response(jsonify(data =data, mean =mean , variance=variance))



	return resp

# This is just a trial for the unittest	
@app.route("/try")
def trials():
	my_query = "SELECT date,price FROM gold_metals WHERE date between '2019-4-1' and '2019-6-1';"
	results = connection.execute(my_query).fetchall()
	r = [dict(row) for row in results]
	dates = [str(ri['date']) for ri in r]
	prices = [float(ri['price'])for ri in r]
	data = dict(zip(dates, prices))
	
	mean =round(sum(prices)/len(prices),2) 
	variance = round(np.var(prices),2)
	
	return jsonify(data =data, mean =mean , variance=variance)
	



# this route helps to deal with the favicon errors
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.debug = True
    
    app.run(host='127.0.0.1', port=8080)
