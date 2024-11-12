from flask import Flask
from routes.gym_routes import gym_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(gym_blueprint, url_prefix="/api/gym")
    return app



if __name__ == '__main__':
    app = create_app()
    app.run()