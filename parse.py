import json
def parse_file(file, limit):
	mylist_2=[]
	if file['total'] < limit:
		i=file['total']
		for k in range(0,i):
			#print('reach')
			if file['businesses'][k]['location']['address1'] is None:
                                my_list=[file['businesses'][k]['name'],'URL: '+file['businesses'][k]['url'],file['businesses'][k]['display_phone'], file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][k]['price'], file['businesses'][k]['review_count'], file['businesses'][k]['location']['display_address'],  file['businesses'][k]['image_url'], file['businesses'][k]['phone']]
			elif 'price' not in file['businesses'][k]:
                               my_list=[file['businesses'][k]['name'],'URL: '+file['businesses'][k]['url'],file['businesses'][k]['display_phone'],file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: N/A', file['businesses'][k]['review_count'],file['businesses'][k]['location']['display_address'],  file['businesses'][k]['image_url'], file['businesses'][k]['phone']]
                        else:    
                                my_list=[file['businesses'][k]['name'],file['businesses'][k]['url'],file['businesses'][k]['display_phone'], file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][k]['price'], file['businesses'][k]['review_count'], file['businesses'][k]['location']['display_address'], file['businesses'][k]['image_url'], file['businesses'][k]['phone']]
			mylist_2.append(my_list)
	else:
		for i in range(0,limit):
	  		#print i
			#print('reach')
			if file['businesses'][i]['location']['address1'] is None:
				my_list=[file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],file['businesses'][i]['display_phone'],file['businesses'][i]['rating'],file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+ file['businesses'][i]['price'],file['businesses'][i]['review_count'],file['businesses'][i]['location']['display_address'],  file['businesses'][i]['image_url'], file['businesses'][i]['phone']]	
			elif 'price' not in file['businesses'][i]: 
                                my_list=[file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],file['businesses'][i]['display_phone'],file['businesses'][i]['rating'], file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: N/A', file['businesses'][i]['review_count'],file['businesses'][i]['location']['display_address'], file['businesses'][i]['image_url'], file['businesses'][i]['phone']]
			else:	
	      			my_list=[file['businesses'][i]['name'],file['businesses'][i]['url'],file['businesses'][i]['display_phone'], file['businesses'][i]['rating'],file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][i]['price'],file['businesses'][i]['review_count'], file['businesses'][i]['location']['display_address'], file['businesses'][i]['image_url'],file['businesses'][i]['phone']]		
			mylist_2.append(my_list)		
	return mylist_2

def parse_more(file, limit,num):
        mylist_2=[]
       
	if num< limit:
                i=num
                for k in range(0,i):
                       
                        if file['businesses'][k]['location']['address1'] is None:
                                my_list=[file['businesses'][k]['name'],'URL: '+file['businesses'][k]['url'],file['businesses'][k]['display_phone'], file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][k]['price'], file['businesses'][k]['review_count'], file['businesses'][k]['location']['display_address'],  file['businesses'][k]['image_url'], file['businesses'][k]['phone']]
                        elif 'price' not in file['businesses'][k]:
                                my_list=[file['businesses'][k]['name'],'URL: '+file['businesses'][k]['url'],file['businesses'][k]['display_phone'],file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: N/A', file['businesses'][k]['review_count'],file['businesses'][k]['location']['display_address'],  file['businesses'][k]['image_url'], file['businesses'][k]['phone']]
                        else:
                                my_list=[file['businesses'][k]['name'],file['businesses'][k]['url'],file['businesses'][k]['display_phone'], file['businesses'][k]['rating'], file['businesses'][k]['coordinates']['latitude'],file['businesses'][k]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][k]['price'], file['businesses'][k]['review_count'], file['businesses'][k]['location']['display_address'], file['businesses'][k]['image_url'], file['businesses'][k]['phone']]
                        mylist_2.append(my_list)
	else:
                for i in range(0,limit):
                        #print i
			#print(file['businesses'][i]['name'])
			#print(file)
                        if file['businesses'][i]['location']['address1'] is None:
                                my_list=[file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],file['businesses'][i]['display_phone'],file['businesses'][i]['rating'],file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+ file['businesses'][i]['price'],file['businesses'][i]['review_count'],file['businesses'][i]['location']['display_address'],  file['businesses'][i]['image_url'], file['businesses'][i]['phone']]
                        elif 'price' not in file['businesses'][i]:
                                my_list=[file['businesses'][i]['name'],'URL: '+file['businesses'][i]['url'],file['businesses'][i]['display_phone'],file['businesses'][i]['rating'], file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: N/A', file['businesses'][i]['review_count'],file['businesses'][i]['location']['display_address'], file['businesses'][i]['image_url'], file['businesses'][i]['phone']]
                        else:
                                my_list=[file['businesses'][i]['name'],file['businesses'][i]['url'],file['businesses'][i]['display_phone'], file['businesses'][i]['rating'],file['businesses'][i]['coordinates']['latitude'],file['businesses'][i]['coordinates']['longitude'],file['region']['center']['longitude'],file['region']['center']['latitude'],'Price: '+file['businesses'][i]['price'],file['businesses'][i]['review_count'], file['businesses'][i]['location']['display_address'], file['businesses'][i]['image_url'],file['businesses'][i]['phone']]
                        mylist_2.append(my_list)
        return mylist_2



def parse_phone(file):
        mylist_2=[]
	if file['businesses'][0]['location']['address1'] is None:
                my_list=[file['businesses'][0]['name'],'URL: '+file['businesses'][0]['url'],'Phone: '+file['businesses'][0]['phone'],file['businesses'][0]['rating'],file['businesses'][0]['coordinates']['latitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['latitude'], 'Price: '+file['businesses'][0]['price'], file['businesses'][0]['review_count'], file['businesses'][0]['location']['display_address'], file['businesses'][0]['image_url']]        	
	elif 'price' not in file['businesses'][0]:  
                my_list=[file['businesses'][0]['name'],'URL: '+file['businesses'][0]['url'],'Phone: '+file['businesses'][0]['phone'],file['businesses'][0]['rating'],file['businesses'][0]['coordinates']['latitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['latitude'],'Price: N/A',file['businesses'][0]['review_count'], file['businesses'][0]['location']['display_address'], file['businesses'][0]['image_url']]
	else: 
       		my_list=[file['businesses'][0]['name'],file['businesses'][0]['url'],'Phone: '+file['businesses'][0]['phone'],file['businesses'][0]['rating'], file['businesses'][0]['coordinates']['latitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['longitude'],file['businesses'][0]['coordinates']['latitude'],'Price: '+ file['businesses'][0]['price'], file['businesses'][0]['review_count'], file['businesses'][0]['location']['display_address'], file['businesses'][0]['image_url']] 			
	mylist_2.append(my_list)           
        
	return mylist_2





