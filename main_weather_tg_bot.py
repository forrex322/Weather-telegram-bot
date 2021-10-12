import requests
import datetime

import telebot

from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "your_token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Я бот. Приятно познакомиться!')


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \0002600",
        "Clouds": "Облачно \0002601",
        "Rain": "Дождь \0002614"
    }

    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = response.json()

        city = data["name"]
        current_temperature = data["main"]["temp"]
        weather = data['weather'][0]['main']
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city} \nТемпература: {current_temperature}C°\n"
              f"Погода: {weather}\nВлажность: {humidity}%\n"
              f"Давление: {pressure} мм.рт.ст\nСкорость ветра: {wind}\n"
              f"Рассвет: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\n"
              f"Хорошего дня!")


    except Exception as ex:
        await message.reply("Please check if the city is entered correctly")


if __name__ == '__main__':
    executor.start_polling(dp)