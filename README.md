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
- git clone git@github.com:Psycadelik/weather_api_app.git
- cd weather_api_app
- python3 -m venv venv
- pip install -r requirements.txt
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

