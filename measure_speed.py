import requests
import time
from io import BytesIO

from urllib3.exceptions import NameResolutionError


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



