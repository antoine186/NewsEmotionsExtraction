import os
import psycopg2

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# postgres://{user}:{password}@{hostname}:{port}/{database-name}
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:login123@localhost:5432/postgres'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False