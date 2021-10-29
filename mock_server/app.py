from flask import Flask
from mock_server.routes import build_routes

def build_app() -> Flask:
    app = Flask(__name__)
    build_routes(app)
    return app
