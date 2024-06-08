import os

import pandas as pd
from flask import Flask, jsonify, send_from_directory


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
        return jsonify(read_csv_to_json(result_file_path))

    return app


def read_csv_to_json(file_path):
    df = pd.read_csv(file_path, names=['time', 'download_duration', 'avg_mbps'], header=None)
    return df.to_dict(orient='records')


