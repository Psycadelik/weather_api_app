import unittest
import json
from unittest.mock import Mock
from django.test import TestCase
from rest_framework.test import RequestsClient
from .views import GetLocationTemperatures
from .weatherapi_artifacts.temperature_data import maximum_temperature
from .weatherapi_artifacts.temperature_data import minimum_temperature
from .weatherapi_artifacts.temperature_data import average_temperature
from .weatherapi_artifacts.temperature_data import median_temperature


class WeatherAppTest(TestCase):
    """ Test fixture """

    def setUp(self):
        self.client = RequestsClient()
        self.weather_api = RequestsClient()
        self.request_params = {
            "location": "Nairobi",
            "days": 5
        }

        self.test_data = [17.5, 28.0, 29, 33]
        self.test_median_data = [34, 20, 19.4]
        self.test_data_array = [11, 12.0]
        self.merged_array = self.test_data + self.test_median_data +\
                            self.test_data_array

        self.test_json_response = {
            "forecast": {
                "forecastday": [
                    {
                        "date": "2021-09-05"
                    },
                    {
                        "date": "2021-09-06"
                    },
                    {
                        "date": "2021-09-07"
                    }
                ]
            }
        }

        self.test_url = 'http://localhost:8000/api/locations/{}/?days={}'. \
            format(self.request_params['location'], self.request_params['days']
                   )

        self.test_api_response = {
            "maximum": 29,
            "minimum": 23,
            "average": 24.5,
            "median": 19
        }

    """ test that the maximum temperature function returns a value """

    def test_maximum_temperature_function(self):
        assert maximum_temperature(self.test_data) == 33

    """ test that the minimum temperature function returns a value """

    def test_minimum_temperature_function(self):
        assert minimum_temperature(self.test_data) == 17.5

    """ test that the average temperature function returns a value """

    def test_average_temperature_function(self):
        assert average_temperature(self.test_data) == 26.875

    """ test that the median temperature function returns a value """

    def test_median_temperature_function(self):
        assert median_temperature(self.merged_array) == 20

    """ test that the weather api returns correct data"""

    def test_weather_api_returns_city_temperature_within_range_of_days(
            self):
        # test the range of days is equal to input(in number of days)
        res_count = len(self.test_json_response['forecast']['forecastday'])
        assert res_count == 3

    """ test that the GetLocations class has its instance methods called """

    def test_get_location_temps_class(self):
        app = GetLocationTemperatures()
        app.get = Mock(return_value=self.test_api_response)

        app.get(self.request_params['location'], self.request_params['days'])

        app.get.assert_called_with(self.request_params['location'],
                                   self.request_params['days'])

    """ Test the api endpoints returns data as expected """

    def test_api_endpoint(self):
        response = self.client.get(self.test_url)
        assert response.status_code == 200
        data = json.loads(response.content)
        self.assertTrue(data['maximum'])
        self.assertTrue(data['minimum'])
        self.assertTrue(data['average'])
        self.assertTrue(data['median'])


if __name__ == '__main__':
    unittest.main()
