class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def addTime(self, hours, minutes, seconds):
        if seconds + self.seconds >= 60:
            self.minutes += ((seconds + self.seconds) // 60)
            self.seconds = (seconds + self.seconds) % 60
        else:
            self.seconds = seconds

        if minutes + self.minutes >= 60:
            self.hours += ((minutes + self.minutes) // 60)
            self.minutes = (minutes + self.minutes) % 60
        else:
            self.minutes += minutes

        if hours + self.hours >= 24:
            self.hours = ((hours + self.hours) % 24)
            
        else:
            self.hours +=hours

    def __str__(self):
            return f"{self.hours}h:{self.minutes}m:{self.seconds}s"
        
    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __add__(self, other):
        watch = Clock(self.hours, self.minutes, self.seconds)
        watch.addTime(other.hours, other.minutes, other.seconds)
        return watch

watch1 = Clock(15 ,20 ,35)
watch2 = Clock(15 ,20 ,35)

print(watch1 == watch2)
print(watch1 + watch2)

print("--------------------------------2-----------------------------------")

class Book:
    def __init__(self, title, autor, pages):
        self.title = title
        self.autor = autor
        self.pages = pages

    def __str__(self):
        return f"Tytuł: \"{self.title}\", książka napisana przez: {self.autor}"

    def __eq__(self, other):
        return self.title == other.title and self.autor == other.autor

    def _radd__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        else:
            return self.pages + other

    def __lt__(self, other):
        if self.pages < other.pages:
            return True
        return False

ksiazka1 = Book("Zaklinacz Czasu", "Andrzej Sapkowski", 134)
ksiazka2 = Book("Cudownie tu i teraz", "Maria Zarii", 345)
ksiazka3 = Book("Miasto Kości", "Frank Cobane", 976)

lista = [ksiazka1, ksiazka2, ksiazka3]

print(sum(lista))

print(ksiazka1 == ksiazka2)

if ksiazka1 < ksiazka3:
    print(f"Książka {ksiazka1} jest cieńsza niż książka {ksiazka2}")
else:
    print(f"Książka {ksiazka2} jest cieńsza niż książka {ksiazka1}")
