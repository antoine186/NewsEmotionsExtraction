from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

with app.app_context():
    db = SQLAlchemy()
    print('bad')

    class User(db.Model):
        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
        age = db.Column(db.String(120))
        password = db.Column(db.String(120))

        @property
        def serialize(self):
            return {
                'id': self.id,
                'name': self.name,
                'city': self.city,
                'state': self.state,
                'password': self.password
            }
