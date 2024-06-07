from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def my_task():
    print('Hallo')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(my_task, 'cron', second='*/1')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
