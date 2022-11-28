class Book:

    def __init__(self, title, autor, pages):
        self.title = title
        self.autor = autor
        self.pages = pages

    def __str__(self):
        return f"Tytuł: \"{self.title}\", książka napisana przez: {self.autor}"

    def __eq__(self, other):
        return self.title == other.title and self.autor == other.autor

    def __radd__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        else:
            return self.pages + other

    def __lt__(self, other):
        if self.pages < other.pages:
            return True
        return False

ksiazka1 = Book("Zaklinacz Czasu","Andrzej Sapkowski", 134)
ksiazka2 = Book("Cudownie tu i teraz", "Maria Zarii", 345)
ksiazka3 = Book("Misto Kości", "Frank Cobane", 976)

lista = [ksiazka1, ksiazka2, ksiazka3]

print(sum(lista))

print(ksiazka1 == ksiazka2)

if ksiazka1 < ksiazka3:
    print(f"Ksiazka {ksiazka1} jest ciensza niz ksiazka {ksiazka2}")
else:
    print(f"Ksiazka {ksiazka2} jest ciensza niz ksiazka {ksiazka1}")