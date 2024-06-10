from apscheduler.schedulers.background import BackgroundScheduler

from app import persistence, flaskr
from app.measurement import measure_download_of_data_and_write_result_to_file

result_file_path_template = './results/{}.csv'


def measurement_job():
    measurement = measure_download_of_data_and_write_result_to_file()
    persistence.save_measurement(measurement)


def create_app():
    # Scheduling has to come before the flask web server
    scheduler = BackgroundScheduler()
    scheduler.add_job(measurement_job, 'cron', second='*/20')
    try:
      scheduler.start()
    except (KeyboardInterrupt, SystemExit):
      pass

    flaskr.create_app(result_file_path_template).run(debug=True, use_reloader=False)
