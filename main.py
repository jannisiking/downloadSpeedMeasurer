import datetime
import time

from apscheduler.schedulers.blocking import BlockingScheduler

from calculate_download_speed import calculate_average_mbit_per_seconds
from measure_speed import measure_speed

time_interval_in_seconds = 20
file_size_description = '100MB'
download_url = 'https://fsn1-speed.hetzner.com/' + file_size_description + '.bin'


def measurement_job():
    timestamp = datetime.datetime.now()
    result = measure_speed(download_url)
    mbit_per_seconds = calculate_average_mbit_per_seconds(result, file_size_description)
    print(timestamp, ' ', result, ' ', mbit_per_seconds)


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(measurement_job, 'cron', second='*/{}'.format(time_interval_in_seconds))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
