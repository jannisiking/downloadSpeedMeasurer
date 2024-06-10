from dataclasses import dataclass


class Measurement:
    def __init__(self, timestamp, duration, avg_mbps):
        self.timestamp = timestamp
        self.duration = duration
        self.avg_mbps = avg_mbps

    def serialize(self):
        return {"timestamp": self.timestamp,
                "duration": self.duration,
                "avg_mbps": self.avg_mbps}