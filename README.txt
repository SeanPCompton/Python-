

Crunchbase Company Data File for Py Script.txt is the full company file to be run through the API

Crunchbase API Script.py is the draft script being written to automate API call to Crunchbase.



API Documentation:  http://developer.crunchbase.com/docs

or to test end points:  http://developer.crunchbase.com/io-docs



Crunchbase sample company page:  http://www.crunchbase.com/company/google



For Script:

We want to run the company name from a data file, search the API, and return the data to a searchable file with Contact First Name, Last Name, Title associated with the Company, Website, Company Phone number.  



#FOR CRUNCHBASE API search we want the Entity Information search end point http://api.crunchbase.com/v/1/company/<COMPANY NAME FROM LIST>.js?api_key=eg2c9hwbgq2ssn8bs2wsc8te and then the:

 # name key
 # phone number key
 # homepage_url
 # relationships key and then:
     #"is_past": false,
        #"title": "XYZ Title",
        #"person": {
         #   "first_name": "XYZ First Name",
         #   "last_name": "XYA Last Name",

 The JSON data will have many values of past employees we don't want where "is_past": true
