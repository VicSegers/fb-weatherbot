#!/usr/bin/python3

from configparser import ConfigParser

from facebook_bot import FacebookBot
from open_weather import OpenWeather


if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')

    city_id = config['OpenWeatherMap']['CityID']
    api_key = config['OpenWeatherMap']['APIKey']
    email = config['Facebook']['Email']
    password = config['Facebook']['Password']
    name = config['Facebook']['FirstName']
    uid = config['Facebook']['UID']

    open_weather = OpenWeather(name, city_id, api_key)
    facebook_bot = FacebookBot(email, password)

    facebook_bot.send_message_to_user(open_weather.get_weather_message(), uid)
