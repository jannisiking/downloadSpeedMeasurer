from apscheduler.schedulers.background import BackgroundScheduler

from app import persistence, flaskr
from app.measurement import measure_download_of_data_and_write_result_to_file


def measurement_job():
    measurement = measure_download_of_data_and_write_result_to_file()
    persistence.save_measurement(measurement)


def create_app():
    # Scheduling has to come before the flask web server
    scheduler = BackgroundScheduler()
    scheduler.add_job(measurement_job, 'cron', minute='*/1')
    try:
      scheduler.start()
    except (KeyboardInterrupt, SystemExit):
      pass

    return flaskr.create_app()
