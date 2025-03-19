from datetime import datetime

class Workout:
    def __init__(self, start_time, end_time, heart_rate, distance):
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")
        self.heart_rate = heart_rate
        self.distance = distance

    def get_duration(self):
        return (self.end_time - self.start_time).seconds / 3600  # Duration in hours
