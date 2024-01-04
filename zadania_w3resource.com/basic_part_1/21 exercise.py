
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = int(input("Podaj liczbę: "))
if num % 2 == 0:
    print(str(num) + " to liczba parzysta")
else:
    print(str(num) + " to liczba nieparzysta")