import requests
import json

api_key = "YOUR_API_KEY"
while True:
    try:
        city = input("Şehir: ")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
        response = requests.get(url)
        data = json.loads(response.text)

        print(f"Şehir: {data['name']}")
        print(f"Sıcaklık: {data['main']['temp']} °C")
        print(f"Nem: {data['main']['humidity']} %")
        print(f"Basınç: {data['main']['pressure']} hPa")
        print(f"Rüzgar: {data['wind']['speed']} m/s")
        print(f"Durum: {data['weather'][0]['description']}")
        break
    except KeyError:
        print("Şehir adını doğru giriniz...")
