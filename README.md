# weather_api_app
An integration to https://weatherapi.com

This is the project structure:
```
.
├── README.md
├── requirements.txt
└── weatherapi_integration
    ├── manage.py
    ├── weatherapi_integration
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── yoyo_weather_app
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        └── weatherapi_artifacts
            ├── fetch_location_weather.py
            └── temperature_data.py
```

Local Setup:
```
1. clone the project:
- git clone git@github.com:Psycadelik/weather_api_app.git

2. cd into the directory:
- cd weather_api_app

3. create a virtual environment:
- python3 -m venv venv

4.activate the virtual environment:
- source venv/bin/activate

5. install required dependecies:
- pip install -r requirements.txt

6. explore the app directory:
- cd weatherapi_integration
```
To run tests:
```
- python manage.py test
```

To run a local server:
```
- python manage.py runserver
```

To test the API endpoint:
- open postman and put in the following as a GET request
`http://127.0.0.1:8000/api/locations/<city-of-your-choice>/?days=(forecasted-number-of-days)`


- view the Json response which should be in the following format:
```
{
    "maximum": <some-value>,
    "minimum": <some-value>,
    "average": <some-value>,
    "median": <some-value>
}
```
NB: note that the weatherapi.com api forecasts for a maximum of 3 days
