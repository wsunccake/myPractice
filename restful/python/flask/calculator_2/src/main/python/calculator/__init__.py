from flask import Flask
from calculator.controllers.main import main_blueprint
from calculator.controllers.base import base_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(base_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
