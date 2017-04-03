# -*- coding: utf-8 -*-
"""
Yelp Fusion API code sample.
This program demonstrates the capability of the Yelp Fusion API
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.
Please refer to http://www.yelp.com/developers/v3/documentation for the API
documentation.
This program requires the Python requests library, which you can install via:
`pip install -r requirements.txt`.
Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib


# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


# OAuth credential placeholders that must be filled in by users.
# You can find them on
# https://www.yelp.com/developers/v3/manage_app
CLIENT_ID = 'u24el7WOE_eevCoQq_b34A'
CLIENT_SECRET = '0nwC1fGOtEbOJtmtBQYJ93OiT6eF0HeMqUU9ZTpK3hbO81alE2iWQ4blmFTTNXnq'

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
PHONE_SEARCH_API_URL = 'https://api.yelp.com/v3/businesses/search/phone'
SEARCH_PATH = '/v3/businesses/search'
PHONE_PATH = '/v3/businesses/search/phone'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
AUTO_PATH= '/v3/autocomplete'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'


def obtain_bearer_token(host, path):
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        str: OAuth bearer token, obtained using client_id and client_secret.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        bearer_token (str): OAuth bearer token, obtained using client_id and client_secret.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

   #print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()

def search_phone(phone):
    """Query the Search API by a phone number.
    Args:
        phone (str): The search number passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    phone=phone.replace('(','')
    phone=phone.replace(')','')
    phone=phone.replace(' ','')
    url_params = {
        'phone': '+1'+phone.replace('-',''), 
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, PHONE_PATH, bearer_token, url_params=url_params)
'''
def auto_location(lat,long,term):
    """Query the Search API by lat/long and autocomplete.
    Args:
        latitude (dec: The search longitude passed to the API.
        longitude (dec): The search latitude passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
   
    url_params = {
    	'text':term.replace(' ','+'), 
   	'latitude': lat,
        'longitude':long,
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, AUTO_PATH, bearer_token, url_params=url_params)
'''
def results_more(offset):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'sort_by': sort
	#'offset': offset
    }

def search(term, location, sort,limit,open, offset):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
	sort (str): The sort method.
	
    Returns:
        dict: The JSON response from the request.
    """
    #int offset=0;
    #if (offset==0):
    if offset+limit<1000:
   	print('ffffff') 
	url_params = {
    	'term': term.replace(' ', '+'),
    	'location': location.replace(' ', '+'),
    	'limit': limit,
    	'offset': offset,
    	'sort_by': sort, 
    	'open_now':open
    	}
    else:
	url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': limit,
        'sort_by': sort,
        'offset': offset,
        'open': open
        }
			
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)


def search_price(term, location, price, sort, limit, open, offset):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        price (str): The search price passed to the API
	sort (str): The sorting way passed
    Returns:
        dict: The JSON response from the request.
    """
    if offset+limit>1000:
	limit=1000-offset
        url_params = {
        	'term': term.replace(' ', '+'),
        	'location': location.replace(' ', '+'),
        	'limit': limit,
        	'price':price.replace(' ','+'),
        	'sort_by': sort,
        	'offset': offset,
        	'open': open
   	}
    else:
    	url_params = {
        	'term': term.replace(' ', '+'),
        	'location': location.replace(' ', '+'),
        	'limit': limit,
        	'price':price.replace(' ','+'),
		'sort_by': sort,
		'offset': offset,
		'open': open
    	}
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)

def search_best(term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        price (str): The search price passed to the API
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'sort_by': 'rating'
    }
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)

def search_most(term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        price (str): The search price passed to the API
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'sort_by': 'review_count'
    }
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)


def get_business(bearer_token, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, bearer_token)

def get_reviews(business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    business_path = BUSINESS_PATH + business_id + '/reviews'

    return request(API_HOST, business_path, bearer_token)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)

    response = search(bearer_token, term, location)

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return
    
    business_id = businesses[0]['id']

    #print(u'{0} businesses found, querying business info ' \
    #    'for the top result "{1}" ...'.format(
    #        len(businesses), business_id))
    response = get_business(bearer_token, business_id)
    return businesses;
    #print(u'Result for business "{0}" found:'.format(business_id))
    #pprint.pprint(response, indent=2)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()#this reads the arguments and parses the arguments
    
    try:#makes the attempt to get the businesses
        query_api(input_values.term, input_values.location)#hits the api to get the info
    except HTTPError as error:#what happens when an error happens
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()
