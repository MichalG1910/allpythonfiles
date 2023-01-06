# instrukcja warunkowa if oczekuje wartości true i tylko wtedy uruchomi kod pod nią.  Kod do wykonania 
# zwyczajowo wpisuje się po 4 spacjach (nasz edytor VSC sam je robi).
num = 5
if num >= 3:
    print( "num większe lub równe 3" )
    print( "oraz !" )                   # uruchomi się również ten wiersz, jeśli ma ten sam poziom zagnieżdżenia

if num == 2:
    print( "num = 2" )
elif num == 1:                  # instrukcja warunkowa elif jest wykonywana, jeśli  if = false. Program 
    print( "num = 1" )          # będzie wykonywał po kolei instrukcje elif, aż któraś z nich zostanie spełniona
elif num == 5:
    print( "num = 5" )
elif num > 0:                   # instrukcja nie została wykonana (mimo tego że jest true), ponieważ wcześniejsza 
    print( " num > 0" )         # instrukcja była prawidlowa i zostala wyświetlona w terminalu
else:
    print( "domyślny kod jeśli reszta porównań da False")
# instrukcja else wwyświetla kod, jeśli wszystkie poprzednie instrukcje if/elif dały wartość False. Po else nie 
# wpisujemy już zadnego warunku tylko piszemy ":"
print( "dalszy kod" )           # ten kod zostanie wyświetlony (jest zagnieżdżony stopień bliżej)

if 5 > 1: print( "5 > 1") # możey zastosować zapis w jednym wierszu tylko dla jednej instrukcji print

if 10 > 2:
    print( "10 > 2" )
    if 3 > 1:
        print( "3 > 1" )
        if 3 < 2:               # False - zostanie pominięte
            print( "3 > 2" )
        print( "cd. 3 > 1" )

print()

print("prawda") if 5 > 2 else print("nieprawda") # prawda

a = "parzysta" if 10 % 2 == 0 else "nieparzysta" # parzysta- przypisanie wyniku instrukcji do zmiennej
print(a)

print(list(range(10)))

for i in range(10): # else odnosi się nie do instrukcji if, lecz do pętli for (może też do while)
    if i > 5:
        continue
else:
    print("koniec")
# wynikiem działanie tej pętli będzie: koniec
# jeśli else odnosiłoby się do if (było na tym samym poziomie zagnieżdżenia), wynikiem byłoby: 6 X koniec

try:
    a = 5/4
except ZeroDivisionError:
    print("Błąd!!! Nie wolno dzielić przez 0!!!")

else:
    print("wszystko gra, nie dzieliłeś przez ZERO")
# zastosowanie else w instrukcji try:except doprowadzi do wykonania else, 
# jeśli nasz sprawdzany wyjątek (błąd) nie wystąpi

print("\n--------1--------if elif else-------------------------------")
# jeśli wykonujemy po sobie kilka instrukcji if to wykonają się one wszystkie po kolei, a zwrócone zostaną tylko True
# jesli po instrukcjach if występuje elif, to zostanie ona sprawdzona tylko wtedy, gdy, żadna z instrukcji 
#   if nie będzie True i nie zostaną one wykonane.
# wykona się tylko pierwsza instrukcja elif = True. Każda kolejna, nawet = True nie zostanie sprawdzona
# po instrukcjach elif możemy sprawdzać instrukcje if. Jeśli = True - zostaną wyświetlone
# instrukcja else zostanie sprawdzona tylko jesli wczesniejsze instrukcje if elif = False. Może ona wystąpić tylko raz
a = 10
print(" sprawdzamy a dla liczby 10")
if a == 10: # True
    print ("a = 10")    # zostanie wyświetlone
if a > 11: # False
    print("a > 11")     #  nie zostanie wyświetlone
if a != 12: # True
    print("a != 12")    # zostanie wyświetlone
elif a < 14: # True
    print("a < 14")     # nie zostanie wyświetlone


a = 10
if a != 10: # False
    print ("a != 10")    # nie zostanie wyświetlone
if a > 11: # False
    print("a > 11")     #  nie zostanie wyświetlone
if a == 12: # False
    print("a == 12")    # nie zostanie wyświetlone
elif a < 14: # True
    print("a < 14")     # zostanie wyświetlone
elif a != 14: # True
    print("a != 14")     # nie zostanie wyświetlone
if a == 10: # True
    print("a == 10")     # zostanie wyświetlone
elif a > 3: # True
    print("a > 3")      # nie zostanie wyświetlone
if a > 5: # True
    print("a > 5")     # zostanie wyświetlone
else:
    print(a = 10)      # nie zostanie wyświetlone

