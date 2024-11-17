from settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'EcommCoupon',
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3306"
    }
}


