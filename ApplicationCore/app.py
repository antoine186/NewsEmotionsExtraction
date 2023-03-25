import sys

from flask import render_template
from flask_migrate import Migrate

sys.path.append('ApplicationCore')

from models.User import db, app

# from routes.user_bp import user_bp

with app.app_context():
    db.init_app(app)
    migrate = Migrate(app, db)

# app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()