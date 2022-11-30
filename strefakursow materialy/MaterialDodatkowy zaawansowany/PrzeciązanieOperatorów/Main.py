class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def addTime(self, hours, minutes, seconds):
        if seconds + self.seconds >= 60:
            self.minutes += ((seconds + self.seconds) // 60)
            self.seconds = (seconds +self.seconds) % 60
        else:
            self.seconds = seconds

        if minutes + self.minutes >= 60:
            self.hours += ((minutes + self.minutes) // 60)
            self.minutes = (minutes + self.minutes) % 60 
        else:
            self.minutes += minutes

        if hours + self.hours >= 24:
            self.hours = ((hours + self.hours) // 24)
        else:
            self.hours += hours

    def __str__(self):
        return f"{self.hours}h:{self.minutes}m:{self.seconds}s"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __add__(self, other):
        watch = Clock(self.hours, self.minutes, self.seconds)
        watch.addTime(other.hours, other.minutes, other.seconds)
        return watch

watch1 = Clock(10,20,0)
watch2 = Clock(10,40,0)

print(watch1 == watch2)
print(watch1 + watch2)

