import sys
sys.path.append('ApplicationCore')
sys.path.append('ApplicationCore/routes')

from app_start_helper import app, db
from main_pages.main_page_blueprint import main_page_blueprint
from authentication.authentication_blueprint import authentication_blueprint
from authentication.session_authentication_blueprint import session_authentication_blueprint

# app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(main_page_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(session_authentication_blueprint)

with app.app_context():
    db.init_app(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
