""" Script for parsing weather forecast on 2nd May 2018 from Yandex.Weather and count forecast error. """

import pandas as pd
import pickle
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def save_to_pickle(data):
    pickle.dump(data, open('data.pickle', 'wb'))


def get_from_pickle():
    return pickle.load(open('data.pickle', 'rb'))


def load_page():
    res = requests.get('https://yandex.ru/pogoda/moscow')
    if res.status_code != 200:
        raise ConnectionError
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def parse_weather_forecast():
    soup = load_page()
    t = soup.select('div[class="forecast-briefly__day forecast-briefly__day_weekend day-anchor i-bem"] '
                    'div[class="temp forecast-briefly__temp forecast-briefly__temp_day"] '
                    'span[class="temp__value"]')[1].text
    t = int(t)
    return t


def parse_weather_fact():
    soup = load_page()
    t = soup.select('div[class="forecast-briefly__day forecast-briefly__day_weekstart_0 day-anchor i-bem"] '
                    'div[class="temp forecast-briefly__temp forecast-briefly__temp_day"] '
                    'span[class="temp__value"]')[0].text
    t = int(t)
    return t


if __name__ == '__main__':
    date_fact = datetime(2018, 5, 2)

    try:
        weather = get_from_pickle()
        # print(weather)
    except FileNotFoundError:
        weather = {}
    if datetime.now() < date_fact:
        # Parse forecast and add it to older data
        temp = parse_weather_forecast()
        weather[datetime.now().strftime(format='%d.%m.%Y')] = temp
        save_to_pickle(weather)
        print('Forecast temperature has been successfully parsed. Run the script tomorrow again.')
    else:
        # Parse real weather only when today >= date_fact
        print("Today is the last day so you'll get the result.")
        fact = parse_weather_fact()
        print(f"Today's temperature is {fact}.")

        # Create dataframe and count error
        df = pd.DataFrame.from_dict(weather, orient='index')
        df.reset_index(inplace=True)
        df.columns = ['date_forecast', 'temperature_forecast']
        df['error'] = (fact - df['temperature_forecast']) / df['temperature_forecast']

        print('\nResult:')
        print(df)
