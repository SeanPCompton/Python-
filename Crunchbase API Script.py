import urllib
import json

f = open('file.txt', 'r')  
for line in f.readlines():
    id = line.strip('\n')
    url = "http://api.crunchbase.com/v/1/company/{0}".format(id) 
    # How do I append ".js?api_key=eg2c9hwbgq2ssn8bs2wsc8teand" on to the end of the above URL?
    urlobj = urllib.urlopen(url)
    try:
        json_data = json.loads(urlobj)
        print json_data
    except:
        print urlobj.readlines()

# How do I now write to a file or save to a database with values organized by keys?


#FOR CRUNCHBASE API search we want the Entity Information search end http://api.crunchbase.com/v/1/company/<COMPANY NAME FROM LIST>.js?api_key=eg2c9hwbgq2ssn8bs2wsc8teand then the:
 # name key
 # phone number key
 # homepage_url
 # relationships key and then:
     #"is_past": false,
        #"title": "XYZ Title",
        #"person": {
         #   "first_name": "XYZ First Name",
         #   "last_name": "XYA Last Name",



