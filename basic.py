import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'

endpoint = 'http://127.0.0.1:2828/api/csv-handler/'
get_response = requests.get(endpoint, json={"query":"Hello World"}) # HTTP Request
print(get_response.text) # print raw text 
#print(get_response.status_code )

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion -> Python Dict
#print(get_response.json())


#  29:31