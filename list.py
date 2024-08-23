import requests
from getpass import getpass

auth_endpoint = 'http://127.0.0.1:2828/django_api/auth/'
password = getpass()

auth_response = requests.post(auth_endpoint, json={"username":"cfe", "password":password}) # HTTP Request
print(auth_response.json()) # print raw text 

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        #"Authorization":f"Token {token}"
        "Authorization":f"Bearer {token}"
    }

    endpoint = 'http://127.0.0.1:2828/django_api/blogposts/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())