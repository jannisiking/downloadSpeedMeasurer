import sqlite3

from model import Measurement


def save_measurement(measurement):
    con = sqlite3.connect('/Users/jannisprivat/PycharmProjects/pythonProject/persistence/database.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO measurements(timestamp, duration, avg_mbps) VALUES (:timestamp, :duration, :avg_mbps)',
                   {"timestamp": measurement.timestamp, "duration": measurement.duration,
                    "avg_mbps": measurement.avg_mbps})
    con.commit()
    cursor.close()
    con.close()

def get_all_measurements():
    con = sqlite3.connect('/Users/jannisprivat/PycharmProjects/pythonProject/persistence/database.db')
    cursor = con.cursor()
    cursor.execute('SELECT timestamp, duration, avg_mbps FROM measurements')
    rows = cursor.fetchall()
    cursor.close()
    con.close()

    measurements = [Measurement(timestamp=row[0], duration=row[1], avg_mbps=row[2]) for row in rows]
    return measurements
