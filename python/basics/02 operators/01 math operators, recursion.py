
a = 12
b = 3

result = a + b; print(result) # 15
result = a - b; print(result) # 9
result = a * b; print(result) # 36
result = a / b; print(result) # 4.0
result = a % b; print(result) # 0 - modulo, czyli reszta bz dzielenia 
result = a % 9; print(result) # 3 - 12/9=1 dziewięć tylko 1 raz zmieści się w całości w 12, 12-9*1=3 wynik=3 reszta z dzielenia
result = a ** b; print(result) # 1728 - podnoszenie do potęgi (12**3)=1728
result = a // b; print(result) # 4 tzw. floor division czyli dzielenie dające tylko liczbę całkowitą jako wynik
result = 20 // 3; print(result) # 6 - 20/3=6.666, wynik to tylko liczba calkowita 6
print("---------")
print(a)
a += 1 # inkrementacja (zwiększanie wartości o 1)
print(a)
print("---------")

# aby policzyć silnie(!) musimy stworzyć funkcję z tzw rekurencją (recursion)
# funkcja rekurencyjna wywołuje samą siebie ze swojego ciała
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)
print(silnia(5)) # !5 = 120
# przebieg operacji: 5 * (5-1=4) * (4-1=3) * (3-1=2) * (2-1=1)
# po podstawieniu za x=5 wykonuje się instrukcja else z zagnieżdżoną kolejną funkcją silnia(x-1).Dopóki
# x będzie > 1 sytuacja będzie się powtarzać . Dopiero w momencie gdy x = 1, zostanie wykonana instrukcja
# if i zostanie zwrócony wynik końcowy