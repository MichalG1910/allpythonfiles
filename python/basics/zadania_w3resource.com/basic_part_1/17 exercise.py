# Write a Python program to test whether a number is  within 100 of 1000 or 2000.

num = float(input("Podaj liczbę: " ))
if num >= 100 and num <= 1000:
    print("Liczba zawiera się w przedziale od 100 do 1000") 

elif num > 1000 and num <= 2000:
    True
    print("Liczba zawiera się w przedziale od 1001 do 2000")
else:
    False
    print("Liczba nie spełnia warunków ćwiczenia")

# źle zrozumiałem zadanie. Mój skrypt pokazuje, czy liczba wprowadzona z klawiatury zawiera się między liczbami 100 a 1000 lub 100 a 2000 i daje odpowiedni komunikat
# Natomiast chodziło o to, żeby sprawdzana liczba zawierała się w przedziale (1000 - 100)= 900 do (2000 - 100) = 1900 czyli od 900 do 1900


def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1900))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))