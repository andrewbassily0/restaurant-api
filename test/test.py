import requests


endpoint= 'https://overapi.com/'

response = requests.get(endpoint , json= {"query"})
print (response.status_code)