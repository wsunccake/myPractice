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


# class Person(db.Model):
#     id = db.Column(db.Integer(), primary_key=True, nullable=False)
#     name = db.Column(db.VARCHAR(20), nullable=False)
#     age = db.Column(db.Integer(), nullable=False)
#     address = db.Column(db.CHAR(25))
#     salary = db.Column(db.DECIMAL(18, 2))
#
#     def __init__(self, name, age, address, salary):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.salary = salary
#
#     def __repr__(self):
#         # formats what is shown in the shell when print is
#         # called on it
#         return '<Name {}>'.format(self.name)


@app.route('/')
def home():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
