from datetime import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        time = datetime.strptime(f"{self.hours}:{self.minutes}:{self.seconds}", "%H:%M:%S")
        return datetime.strftime(time, "%H:%M:%S")

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        else:
            if self.minutes < Time.max_minutes:
                self.minutes += 1
                self.seconds = 0
            else:
                if self.hours < Time.max_hours:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
                else:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
