import requests

response = requests.get('https://api.github.com/users/tjfaccipieri')

print(response.json())