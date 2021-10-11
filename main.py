import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \0002600",
        "Clouds": "Облачно \0002601",
        "Rain": "Дождь \0002614"
    }

    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = response.json()
        pprint(data)

        city = data["name"]
        current_temperature = data["main"]["temp"]
        weather = data['weather'][0]['main']
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city} \nТемпература: {current_temperature}C°\n"
              f"Погода: {weather}\nВлажность: {humidity}%\n"
              f"Давление: {pressure} мм.рт.ст\nСкорость ветра: {wind}\n"
              f"Рассвет: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\n"
              f"Хорошего дня!")


    except Exception as ex:
        print(ex)
        print("Please check if the city is entered correctly")


def main():
    city = input("Enter city: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()