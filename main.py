from apscheduler.schedulers.background import BackgroundScheduler

from flaskr import create_app
from measurement import measure_download_of_data_and_write_result_to_file

result_file_path = './results.csv'


def measurement_job():
    measure_download_of_data_and_write_result_to_file(result_file_path)


if __name__ == '__main__':
    # Scheduling has to come before the flask web server
    scheduler = BackgroundScheduler()
    scheduler.add_job(measurement_job, 'cron', second='*/20')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

    create_app(result_file_path).run(debug=True)
