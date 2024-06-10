import datetime
import time
from io import BytesIO

import requests

from app.model import Measurement

download_url = 'https://fsn1-speed.hetzner.com/100MB.bin'


def measure_speed(url, timeout_in_seconds):
    try:
        start_time = time.time()  # Startzeit messen
        response = requests.get(url, stream=True, timeout=timeout_in_seconds)
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        buffer = BytesIO()

        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                buffer.write(chunk)
                downloaded_size += len(chunk)
                print(f'Downloaded {downloaded_size} of {total_size} bytes', end='\r')

        end_time = time.time()  # Endzeit messen
        elapsed_time = end_time - start_time

        buffer.seek(0)  # Zurück zum Anfang des BytesIO-Objekts, falls benötigt
        return elapsed_time
    except Exception as e:
        print(e)
        return 0


def calculate_average_mbit_per_seconds(speed_in_seconds):
    return calculate_with_bits(speed_in_seconds, 838860800)


def calculate_with_bits(speed_in_seconds, file_size_in_bits):
    if speed_in_seconds == 0:
        return 0
    return (file_size_in_bits / speed_in_seconds)/1000/1000


def measure_download_of_data_and_write_result_to_file():
    timestamp = datetime.datetime.now()
    duration = 0
    mbit_per_seconds = 0
    try:
        print('timestamp: {}'.format(timestamp))
        duration = measure_speed(download_url, 15)
        print('duration: {}'.format(duration))
        mbit_per_seconds = calculate_average_mbit_per_seconds(duration)
        print('mbps: {}'.format(mbit_per_seconds))
    except Exception as e:
        print('Exception: {}'.format(e))

    return Measurement(
        timestamp=timestamp,
        duration=duration,
        avg_mbps=mbit_per_seconds
    )
