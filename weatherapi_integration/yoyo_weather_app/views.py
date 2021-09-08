from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .weatherapi_artifacts.temperature_data import maximum_temperature
from .weatherapi_artifacts.temperature_data import minimum_temperature
from .weatherapi_artifacts.temperature_data import average_temperature
from .weatherapi_artifacts.temperature_data import median_temperature
from .weatherapi_artifacts.fetch_location_weather import \
    fetch_location_weather_data


class GetLocationTemperatures(APIView):
    def get(self, request, *args, **kwargs):
        # 1. fetch the city and number of days from the request params
        # 2. Validate the inputs
        # 3. Call function to fetch location weather data from
        # https://weatherapi.com
        # 4. call functions to compute max,min,avg and median temps
        # 5. return response with given format structure
        # 6. create a browsable api that is accessible locally
        try:
            days = self.request.query_params.get('days')
            location = kwargs.get('location')

            # validate the query params
            if not location:
                response_object = {
                    "status": "error",
                    "message": "please provide a location to fetch weather"
                               " data for"
                }
                return Response(response_object,
                                status=status.HTTP_401_UNAUTHORIZED)

            if not days:
                response_object = {
                    "status": "error",
                    "message": "please provide number of days to get weather "
                               "data range"
                }
                return Response(response_object,
                                status=status.HTTP_401_UNAUTHORIZED)

            # call the fetch location data function to fetch data from
            # https://weatherapi.com
            weather_data = fetch_location_weather_data(location, days)

            # create empty arrays to store the temperatures
            max_temperatures = []
            min_temperatures = []
            avg_temperatures = []

            # loop through the temperatures given in degrees celsius for the
            # location
            for temp in weather_data['forecast']['forecastday']:
                # append the temperatures into the array
                max_temperatures.append(temp['day']['maxtemp_c'])
                min_temperatures.append(temp['day']['mintemp_c'])
                avg_temperatures.append(temp['day']['avgtemp_c'])

            merged_array = max_temperatures + min_temperatures + \
                           avg_temperatures

            response_object = {
                "maximum": maximum_temperature(max_temperatures),
                "minimum": minimum_temperature(min_temperatures),
                "average": average_temperature(avg_temperatures),
                "median": median_temperature(merged_array)
            }

            return Response(response_object, status=status.HTTP_200_OK)

        except Exception as e:
            response_object = {
                "status": "error",
                "message": "an error occured: " + str(e)
            }

            return Response(response_object,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
