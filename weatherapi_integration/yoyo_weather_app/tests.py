import unittest
import mock
from unittest.mock import Mock
from django.test import TestCase
from .weatherapi_artifacts.temperature_data import maximum_temperature
from .weatherapi_artifacts.temperature_data import minimum_temperature
from .weatherapi_artifacts.temperature_data import average_temperature
from .weatherapi_artifacts.temperature_data import median_temperature


class WeatherAppTest(TestCase):
    """ Test fixture """
    def setUp(self):
        self.request_params = {
            "city": "Nairobi",
            "days": 5
        }

        self.test_data = [17.5, 28.0, 29, 33]

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
        assert median_temperature(self.test_data) == 28.5

    """ test that the weather api returns correct data"""
    def test_weather_api_returns_city_temperature_within_range_of_days(
            self):
        pass

    """ test that the weather locations endpoint returns a response """
    def test_weather_locations_api_endpoint(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {


        }
        # test_request.get.side_effect = [Timeout, ]
        # assert


if __name__ == '__main__':
    unittest.main()
