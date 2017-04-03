from flask import Flask
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def home():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
