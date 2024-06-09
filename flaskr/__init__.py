import datetime
import os

import pandas as pd
from flask import Flask, jsonify, send_from_directory, request

import persistence


def create_app(result_file_path):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def serve_static_files(path):
        return send_from_directory(app.static_folder, path)

    @app.route('/data')
    def data():
        from_timestamp = request.args.get('from_timestamp', datetime.datetime.now().replace(hour=0, minute=0, second=0))
        to_timestamp = request.args.get('to_timestamp', datetime.datetime.now())
        measurements = persistence.get_all_measurements(from_timestamp, to_timestamp)
        return jsonify([m.serialize() for m in measurements])

    return app

