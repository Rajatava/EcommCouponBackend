# Ecommerce Coupon Management System

Steps to run the project.

-   Create a Virtual Env : python -m venv env
-   Activate the Env : source env/bin/activate
-   Install packages : pip install -r requirements.txt
-   in settings/dev.py , update DATABASES constant or create a database instance as mentioned
    there :
    {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'EcommCoupon',
    "USER": "root",
    "PASSWORD": "password",
    "HOST": "localhost",
    "PORT": "3306"
    }
-   Rename .env.sample to .env (.env for local setup has been provided at .env.sample)
-   Run Command : python manage.py migrate
-   Run Command : python manage.py runserver
-   Run Command : source up.sh
