import requests
from getpass import getpass


headers = {'Authorization':'Bearer e31560f6dff7d486db8484329af13e28ef4713a1'}
endpoint = 'http://127.0.0.1:2828/django_api/blogposts/'


data = {
    'title':'This is field is done',
    'price': 50,
    'content': 'description random'
}

get_response = requests.post(endpoint, json=data, headers=headers)
get_response = requests.post(endpoint, headers=headers)

print(get_response.json())

#2:57
#https://www.youtube.com/watch?v=c708Nf0cHrs