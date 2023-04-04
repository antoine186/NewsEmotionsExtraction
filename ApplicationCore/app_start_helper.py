from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sys
from DependenciesResources.containers import Container

from DependenciesResources.resources_paths import ResourcesPath
from dependency_injector.wiring import inject, Provide

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
migrate = Migrate(app, db)

container = Container()
container.wire(modules=[sys.modules[__name__]])

paths = Container.resources_path()
nn = Container.pipeline_neural_network()
model_max_tokens_allowed = 512
