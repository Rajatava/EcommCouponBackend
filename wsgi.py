"""
WSGI config for TrueCaller project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from config import SETTINGS_PATH

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_PATH)

application = get_wsgi_application()
