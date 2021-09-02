from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .weatherapi_artifacts.temperature_data import maximum_temperature
from .weatherapi_artifacts.temperature_data import minimum_temperature
from .weatherapi_artifacts.temperature_data import average_temperature
from .weatherapi_artifacts.temperature_data import median_temperature
from .weatherapi_artifacts.fetch_location_weather import fetch_location_weather_data


# API endpoint to fetch locations
@api_view(['GET', 'POST'])
def get_location_temperatures(location, days):
    # 1. fetch the city and number of days from the request params
    # 2. Validate the inputs
    # 3. Call function to fetch location weather from weatherapi.com
    # 4. call functions to compute max,min,avg and median temps
    # 5. return response with given format structure
    # 6. create a browsable api that is accessible locally
    try:
        # validate the query params
        if location == "":
            response_object = {
                "status": "error",
                "message": "please provide a location to fetch weather data "
                           "for"
            }
            return Response(response_object,
                            status=status.HTTP_401_UNAUTHORIZED)

        if days == "":
            response_object = {
                "status": "error",
                "message": "please provide number of days to get weather "
                           "data range"
            }
            return Response(response_object,
                            status=status.HTTP_401_UNAUTHORIZED)

        # call the fetch location data function to fetch data
        weather_data = fetch_location_weather_data(location, days)

        # create an empty array to store the temperatures
        temperatures = []

        # loop through the temperatures given in degrees celsius for the
        # location
        for temp in weather_data.temps:
            # append the temperatures into the array
            temperatures.append(temp)

        response_object = {
            "maximum": maximum_temperature(temperatures),
            "minimum": minimum_temperature(temperatures),
            "average": average_temperature(temperatures),
            "median": median_temperature(temperatures)
        }

        return Response(response_object, status=status.HTTP_200_OK)

    except Exception as e:
        response_object = {
            "status": "error",
            "message": "an error occured: " + str(e)
        }

        return Response(response_object,
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
