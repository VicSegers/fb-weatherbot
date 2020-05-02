import emojis
import requests


class OpenWeather():
    def __init__(self, name, city_id, api_key):
        self.name = name
        self.url = f'http://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}&units=metric'
        self.icons = {
            '01d': ':sunny:',
            '02d': ':sunny:',
            '03d': ':partly_sunny:',
            '04d': ':cloud:',
            '09d': ':umbrella:',
            '10d': ':umbrella:',
            '11d': ':zap:',
            '13d': ':snowflake:',
            '50d': ':foggy:',
            '01n': ':sunny:',
            '02n': ':sunny:',
            '03n': ':partly_sunny:',
            '04n': ':cloud:',
            '09n': ':umbrella:',
            '10n': ':umbrella:',
            '11n': ':zap:',
            '13n': ':snowflake:',
            '50n': ':foggy: '
        }

    def get_weather_message(self):
        weather_json = self.__get_weather_json()
        return self.__generate_message_from_json(weather_json)

    def __get_weather_json(self):
        request = requests.get(self.url)
        return request.json()

    def __generate_message_from_json(self, weather_json):
        greeting = f'Good morning {self.name}! Today\'s weather forecast in {self.__get_location(weather_json)}:\n\n'
        forecast = [
            f'{self.__get_hour(block)}  {self.__get_temp(block)} °C  {self.__get_emoji(block)} {self.__get_description(block)}' for block in weather_json['list'][:6]]
        return emojis.encode(greeting + '\n'.join(forecast))

    def __get_location(self, message):
        return message['city']['name']

    def __get_hour(self, block):
        return block['dt_txt'].split(' ')[1][:5]

    def __get_temp(self, block):
        return str(int(round(float(block['main']['temp'])))).rjust(2, ' ')

    def __get_emoji(self, block):
        return self.icons[block['weather'][0]['icon']]

    def __get_description(self, block):
        return block['weather'][0]['description']
