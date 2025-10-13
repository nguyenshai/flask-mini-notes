# app/cofig.py

import os

# Path for project dynamic
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')

# make folder instance if don't have it
os.makedirs(INSTANCE_DIR, exist_ok=True)

# Secret Key: Take from environment variable
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(INSTANCE_DIR, 'db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False