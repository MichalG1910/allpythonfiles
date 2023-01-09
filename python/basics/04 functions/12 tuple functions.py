# tuple functions - funkcje krotki

tuple1 = (0,1,2,3,4) + (5,) + tuple([6,7]) # (0, 1, 2, 3, 4, 5, 6, 7) twozrenie nowej krotki z 2 krotek i listy
print(type(tuple1))
print(tuple1)

print((1,2) * 4) # (1, 2, 1, 2, 1, 2, 1, 2) zwielokrotnienie krotki

print( 9 in tuple1 ) # False - czy 9 jest w krotce tuple1
print( 6 in tuple1 ) # True

print(" ")

print(tuple1[2]) # 2 - zwraca 3 eleent krotki ( elementy numerowane są od 0)
print(len(tuple1)) # 8 - ile elementów jest w krotce
print(min(tuple1)) # 0 - nalmniejszy element krotki
print(max(tuple1)) # 7 - największy element krotki
print("elementów: ", tuple1.count(6)) # elementów:  1 - zlicza ilość wystąpień wartości 6 w krotce
print(tuple1.count(6)) # 1 - zlicza ilość wystąpień wartości 6 w krotce
print("index: ", tuple1.index(6)) # index:  6 -pokazuję indeks wystąpienia wartości 6 w krotce indeksując od 0

exam_st_date = (11,12,2014)
print(type(exam_st_date)) # <class 'tuple'>
print( "The examination will start from : %i / %i / %i"%exam_st_date)
# The examination will start from : 11 / 12 / 2014
# metoda wyciągnięcia z krotki danych

print(tuple1) # (0, 1, 2, 3, 4, 5, 6, 7)
print(sum(tuple1)) # 28, suma poszczególnych argumentów krotki

a, b, c, d, e, f, g, h = tuple1 # tworzenie uproszczone wielu zmiennych zawartych w krotce
print(a) # 0
print(e) # 4
print(g) # 6
print("a:{}, b:{}, c:{}, d:{}, e:{}, f:{}, g:{}, h:{}".format(a,b,c,d,e,f,g,h)) # a:0, b:1, c:2, d:3, e:4, f:5, g:6, h:7
print("a:%s, b:%s, c:%s, d:%s, e:%s, f:%s, g:%s, h:%s"%(tuple1)) # a:0, b:1, c:2, d:3, e:4, f:5, g:6, h:7
# drugi sposób jest kompatybilny ze starszym Pythonem 2
print()

# unboxing (rozpakowywanie) krotki- można stosować też dla innych kolekcji(np list)

a, b = (2, 5)
print(a) #2
print(b) #5

x = 10
y = 20
x, y = y, x
print("x: ", x) # x: 20
print("y: ", y) # y: 10

start, *wszystko, koniec = (1,2,3,4,5,6,7,8,9) # * działa tak, że zmienna *wszystko może wziąć nieskończenie 
# wiele argumentów i zostaną one wyświetlone w [liście]. Jeśli do jeszcze inne zmienne j.w , to one pobiorą 
# sobie odpowiednie argumenty zdodnie z ich indeksem
print(start) # 1
print(wszystko) # [2, 3, 4, 5, 6, 7, 8]
print(koniec)# 9