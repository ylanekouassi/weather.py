import requests

api_key ="dec97d8ebbe5dae57315a0b61d3abbda"
api_url = "https://api.openweathermap.org/data/2.5/weather" #?q={city name}&appid={API key} removed = weather now

response = requests.get(
    url=api_url,
    params={
        "q": "Ottawa",
        "appid": api_key,
                }
)

weather = response.json()
print(weather)