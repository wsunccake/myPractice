from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)


class User(db.Model):
    # __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


@app.route('/')
def home():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
