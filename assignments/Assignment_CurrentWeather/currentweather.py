
import requests

latitude = 51.898
longitude = -8.4706

# Define the URL for the JSON API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_direction_10m"

# Send a GET request to the API
response = requests.get(url)

# Parse the JSON data
data = response.json()

# check connection
# print(data)

# Extract and print the current data
current_temperature = data["current"]["temperature_2m"]
current_wind_direction = data["current"]["wind_direction_10m"]

print("Current temperature: ", current_temperature, chr(176)+"C")
print("Current wind direction: ", current_wind_direction)
