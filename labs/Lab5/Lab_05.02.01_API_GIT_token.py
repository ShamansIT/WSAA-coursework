import requests
import json
from config import apiKey

url = 'https://api.github.com/repos/ShamansIT/aprivateone'

response = requests.get(url, auth=('token', apiKey))
repoJSON = response.json()
# print (response.json())

with open("labs\Lab5\\token.pdf", 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
