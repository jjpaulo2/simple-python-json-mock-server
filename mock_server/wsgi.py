from mock_server.app import build_app

flask_app = build_app()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=True)