import os
import psycopg2

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#stripe_api_key = 'sk_test_51MyG0LFAAs2DFWSVpgT2ghJhCoQnlrO1Y3F29CHsGJkpyaZ8Qo5b7V2hRn8cLmqj4pWmYAI0eLKGWBZubjDsn8cw00or9QmyMd'
stripe_api_key = 'pk_test_51MyG0LFAAs2DFWSVSYjOg0bO20EGAVi3LDtGBypqn3ScKzcn9fV9FpC0QmMHWNw9L831L3R1X7xo4Xf6K2yplsh600khIw33yT'

# Connect to the database
# postgres://{user}:{password}@{hostname}:{port}/{database-name}
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:login123@localhost:5432/postgres'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Emocritical186@database-3.ccigqpo72mbx.us-east-2.rds.amazonaws.com:5432/postgres'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False