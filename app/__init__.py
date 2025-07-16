import os
from flask import Flask, Response, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/env.js')
    def env_js():
        api_url = os.environ.get('API_URL', '')
        api_key = os.environ.get('API_KEY', '')
        js = f"window.API_URL = '{api_url}';\nwindow.API_KEY = '{api_key}';"
        return Response(js, mimetype='application/javascript')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app 