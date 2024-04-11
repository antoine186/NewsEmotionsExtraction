import os
import psycopg2

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

stripe_api_key = ''

# This is for prod
# stripe_api_key = ''

# Connect to the database
# postgres://{user}:{password}@{hostname}:{port}/{database-name}
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:login123@localhost:5432/postgres'

# This is for prod
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Emocritical186@database-3.ccigqpo72mbx.us-east-2.rds.amazonaws.com:5432/postgres'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
