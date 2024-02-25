import requests
import json

# Assuming config.py contains your GitHub API key
from config import apiKey
from config import token

url = 'https://api.github.com/repos/ShamansIT/aprivateone'

# Make the request with authentication
response = requests.get(url, headers={"Authorization": f"{token} {apiKey}"})
repoJSON = response.json()

# Print detailed information about the repository
print(json.dumps(repoJSON, indent=4))
