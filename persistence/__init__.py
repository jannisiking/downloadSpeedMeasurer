import sqlite3


def save_measurement(measurement):
    con = sqlite3.connect('/Users/jannisprivat/PycharmProjects/pythonProject/persistence/database.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO measurements(timestamp, duration, avg_mbps) VALUES (:timestamp, :duration, :avg_mbps)',
                   {"timestamp": measurement.timestamp, "duration": measurement.duration,
                    "avg_mbps": measurement.avg_mbps})
    con.commit()
    cursor.close()
    con.close()
