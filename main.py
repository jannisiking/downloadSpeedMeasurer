import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from calculate_download_speed import calculate_average_mbit_per_seconds
from measure_speed import measure_speed

file_size_description = '100MB'
download_url = 'https://fsn1-speed.hetzner.com/' + file_size_description + '.bin'


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

    f = open('./results.txt', 'a')
    print('Writing to file: {}'.format(loggable_output))
    f.writelines(['\n', loggable_output])
    f.close()


if __name__ == '__main__':
    scheduler = BlockingScheduler() # Change to BackgroundScheduler when there is an API endpoint that is running in foreground

    scheduler.add_job(measurement_job, 'cron', second='*/20')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
