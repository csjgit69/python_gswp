# Calling a JSON API
# 
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points
# 
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# 
# http://py4e-data.dr-chuck.net/geojson?
# This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
# To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py
# 
# Test Data / Sample Execution
# 
# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".
# 
# $ python3 solution.py
# Enter location: South Federal UniversityRetrieving http://...
# Retrieved 2101 characters
# Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok
# Turn In
# 
# Please run your program to find the place_id for this location:
# 
# Xavier University
# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJ0zt ..."
# Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        #address = 'South Federal University'
        address = 'Xavier University'

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    pID = js["results"][0]['place_id']
    print("====================")
    print('lat', lat, 'lng', lng)
    print("Place ID:",pID)
    location = js['results'][0]['formatted_address']
    print(location)
    
