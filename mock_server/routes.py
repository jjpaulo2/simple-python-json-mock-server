from flask import Flask
from mock_server.parser import route

def build_routes(app: Flask):
    route(app, route='/', mock_name='example')