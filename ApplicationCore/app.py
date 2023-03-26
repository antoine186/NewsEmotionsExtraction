import sys
sys.path.append('ApplicationCore')
sys.path.append('ApplicationCore/routes')

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from main_pages.main_page_blueprint import main_page_blueprint
from authentication.authentication_blueprint import authentication_blueprint

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
migrate = Migrate(app, db)

# app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(main_page_blueprint)
app.register_blueprint(authentication_blueprint)

with app.app_context():
    db.init_app(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
