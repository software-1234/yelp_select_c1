import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import logging
from flask import json,Flask,render_template,request,jsonify

import api_yelp
import parse
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/api/search')
def search():
    return render_template('form.html')


@app.route('/api/search',methods = ['POST'])
def index():   
    #food = request.values.get('food')
    #print('hi')
    #print(request.method)
    #print(request.form['term'])
    #print(request.form['term'])
    
    offset=int(request.form['offset'])
    #print(offset)    
    if request.method=='POST':
	if offset==0:
		business_list=[]
		#print(request.form['term'])
		#print(request.form.get('term'))
		phone=request.form['phone']
		
		if phone:
			businesses = api_yelp.search_phone(phone)
			businesses=parse.parse_phone(businesses)    
        		return render_template("results.html",my_list=businesses,num_businesses=1)
        
		open=request.form.get('open')
		term=request.form['term']
		place=request.form['place']
	        if open:
			open=True
		else:
			open=False
        #price=request.form.get('price1')
		price1=request.form.get('price1')
        	price2=request.form.get('price2')
		price3=request.form.get('price3')
		price4=request.form.get('price4')
		#auto=request.form.get('auto')
        	limit=int(request.form['limit'])	
		#print(limit)
		#print(places)
		default=request.form['default']
		price=''
		if price1:
			price='1'
		if price2:
			if price=='':
				price='2'
			else:
				price=price+',2'
		if price3:
			if price=='':
                        	price='3'
                	else:
                        	price=price+',3'
		if price4:
			if price=='':
                        	price='4'
                	else:
                        	price=price+',4'
	
		#print(price)
		if price:
			businesses = api_yelp.search_price(term,place,price,default,limit,open,offset)
		else:
			businesses = api_yelp.search(term,place,default,limit,open,offset)
 		#print(businesses)
		num_businesses=businesses["total"]
		if num_businesses==0:
			return render_template("no_results.html")
		#print(num_businesses)
		num_businesses=int(num_businesses)
		#print(num_businesses)
		#print(limit)	
		offset+=limit
		if phone:
        		businesses=parse.parse_phone(businesses)		
		else:
 			businesses=parse.parse_file(businesses, limit)

	
	
      		place=place.title()
		return render_template("results.html",my_list=businesses,num_businesses=num_businesses,default=default,offset=offset,price=price,open=open,place=place,term=term,limit=limit)
    	elif offset>0:
		#print("reach")
                business_list=[]
                
                open=request.form.get('open')
                term=request.form['term']
                place=request.form['place']
        
                price=request.form.get('price')
                num_businesses=request.form.get('num_businesses') 
                #auto=request.form.get('auto')
                limit=int(request.form['limit'])
                #print(limit)
                #print(places)
                default=request.form['default']
                offset=int(request.form['offset'])
	        
		if price:
                        businesses = api_yelp.search_price(term,place,price,default,limit,open,offset)
                else:
                        businesses = api_yelp.search(term,place,default,limit,open,offset)
                #print(businesses["total"])
		num_businesses=businesses["total"]
                #print(offset)
		num_businesses=int(num_businesses)
		if num_businesses==0:
                        return render_template("no_results.html")
                else:
                        businesses=parse.parse_more(businesses, limit,num_businesses-offset)
		offset+=limit
                place=place.title()
		#current=num_businesses-offset
                return render_template("results.html",my_list=businesses,default=default,num_businesses=num_businesses,offset=offset,price=price,open=open,place=place,term=term,limit=limit)
	



@app.errorhandler(500)
def page_not_found(e):
    return render_template('bad_search.html')   

@app.errorhandler(400)
def page_not_found(e):
    return render_template('bad_search.html')

if __name__=="__main__":	
     app.run(debug=True)
