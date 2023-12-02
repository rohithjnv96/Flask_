from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'SECRET_KEY'

    from Flask_AT.main.app import main
    app.register_blueprint(main)

    return app
