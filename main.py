import datetime
import time

from apscheduler.schedulers.blocking import BlockingScheduler
from measure_speed import measure_speed

size = '100MB'
download_url = 'https://fsn1-speed.hetzner.com/'+size+'.bin'

def measurement_job():
    timestamp = datetime.datetime.now()
    result = measure_speed(download_url)
    print(timestamp, '       ', result)


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(measurement_job, 'cron', second='*/10')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
