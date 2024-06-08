import os

import pandas as pd
from flask import Flask, jsonify


def create_app(result_file_path):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():
        return jsonify(read_csv_to_json(result_file_path))

    return app


def read_csv_to_json(file_path):
    df = pd.read_csv(file_path, names=['time', 'download_duration', 'avg_mbps'], header=None)
    return df.to_dict(orient='records')


