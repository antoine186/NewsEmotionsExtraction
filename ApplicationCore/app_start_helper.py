from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

CORS(app, origins=['http://localhost:19006'])

db = SQLAlchemy()
migrate = Migrate(app, db)
