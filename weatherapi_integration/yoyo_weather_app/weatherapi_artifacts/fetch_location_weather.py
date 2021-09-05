import requests
from django.conf import settings


def fetch_location_weather_data(location, number_of_days):
    # url to make request to
    res = requests.get("https://api.weatherapi.com/v1/forecast.json?key=" \
          "{}&q={}&days={}&aqi=no&alerts=no".format(settings.API_KEY, location,
                                                    number_of_days))

    if res.status_code == 200:
        return res.json()
    return None
