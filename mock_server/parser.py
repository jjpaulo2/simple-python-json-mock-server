import json
from flask import Flask, jsonify, Response
from mock_server.responses import MockNotFoundResponse

def mock_parser(mock_name: str) -> dict:
    try:
        with open(f'mock_server/responses/{mock_name}.json', 'r') as mock_file:
            file_content = mock_file.read()
            return json.loads(file_content)

    except FileNotFoundError:
        return MockNotFoundResponse(
            message='Mock not found',
            mock=mock_name
        ).dict()

def route(app: Flask, route: str, mock_name: str) -> Response:
    mock_response = mock_parser(mock_name)

    def get_mock():
        return jsonify(mock_response)

    get_mock.__name__ = f'get_{mock_name}'
    app.get(route)(get_mock)
