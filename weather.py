import requests

api_key ="dec97d8ebbe5dae57315a0b61d3abbda"
api_url = "https://api.openweathermap.org/data/2.5/weather" #?q={city name}&appid={API key} removed = weather now

city = input("Enter the city: ")

response = requests.get(
    url=api_url,
    params={
        "q": city,
        "appid": api_key,
        "units": "metric"
                }
)

weather = response.json()
print("The temperature is:", weather["main"]["temp"])