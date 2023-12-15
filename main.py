import requests
import json

api_key = "YOUR_API_KEY"
while True:
    try:
        city = input("Enter city name: ")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"
        response = requests.get(url)
        data = json.loads(response.text)

        print(f"City: {data['name']}")
        print(f"Temp: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']} %")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Description: {data['weather'][0]['description']}")
        break
    except KeyError:
        print("Enter the correct city name...")
