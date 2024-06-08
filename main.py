import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify

from calculate_download_speed import calculate_average_mbit_per_seconds
from measure_speed import measure_speed
import pandas as pd

app = Flask(__name__)

file_size_description = '100MB'
download_url = 'https://fsn1-speed.hetzner.com/' + file_size_description + '.bin'
result_file_path = './results.csv'


def read_csv_to_json(file_path):
    df = pd.read_csv(file_path, names=['time', 'download_duration', 'avg_mbps'], header=None)
    return df.to_dict(orient='records')


@app.route('/')
def hello_world():
    return jsonify(read_csv_to_json(result_file_path))


def measurement_job():
    timestamp = datetime.datetime.now()
    try:
        result = measure_speed(download_url, 15)
        print('result: {}'.format(result))
        mbit_per_seconds = calculate_average_mbit_per_seconds(result, file_size_description)
        print('mbps: {}'.format(mbit_per_seconds))
        loggable_output = '{},{},{}'.format(timestamp, result, mbit_per_seconds)
        print('loggable_output: {}'.format(loggable_output))
    except Exception as e:
        print('Exception: {}'.format(e))
        loggable_output = '{},0,0'.format(timestamp)

    try:
        f = open(result_file_path, 'a')
        print('Writing to file: {}'.format(loggable_output))
        f.writelines(['\n', loggable_output])
        f.close()
    except Exception as e:
        print('Writing to file failed: {}'.format(e))


if __name__ == '__main__':
    # Scheduling has to come before the flask web server
    scheduler = BackgroundScheduler()
    scheduler.add_job(measurement_job, 'cron', second='*/20')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

    app.run(debug=True)
