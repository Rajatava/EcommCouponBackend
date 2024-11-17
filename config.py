import json
import os
import dotenv
from constants.base import *
dotenv.read_dotenv()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = os.environ['ENVIRONMENT']
if ENVIRONMENT == 'dev':
    SETTINGS_PATH = 'settings.dev'
elif ENVIRONMENT == 'prod':
    SETTINGS_PATH = 'settings.prod'
else:
    raise ValueError("Invalid or unspecified environment")