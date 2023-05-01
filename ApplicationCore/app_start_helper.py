from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sys
from DependenciesResources.containers import Container
from flask_mail import Mail, Message

from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "noreply@emomachines.xyz"
app.config['MAIL_PASSWORD'] = "jdztxwrikhatwrcn"

mail = Mail(app)

CORS(app, supports_credentials=True)

db = SQLAlchemy()
migrate = Migrate(app, db)

container = Container()
container.wire(modules=[sys.modules[__name__]])

paths = Container.resources_path()
nn = Container.pipeline_neural_network()
model_max_characters_allowed = 900
