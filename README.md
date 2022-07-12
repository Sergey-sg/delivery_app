# Delivery App

#### application for orders in partner stores and delivery

## Getting started

#### clone repository
#### cd to root directory of project
#### pip install pipenv
#### pipenv install -r requirements.txt
#### create a .env file in the folder delivery_app where the settings are located
#### update .env with your:
    SECRET_KEY='your-secret-key'
    EMAIL_HOST_USER='your-email-host'
    EMAIL_HOST_PASSWORD='your-password'
    GOOGLE_MAPS_API_KEY='yor-google-maps-api'

#### pipenv shell

    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic

    python manage.py runserver

#### https://localhost:8000