import requests
import time

url = 'https://www.google.com'
response = requests.get(url)
print(response)