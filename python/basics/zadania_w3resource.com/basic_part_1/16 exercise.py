# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

num = 17
numYour = int(input("Podaj liczbę całkowitą: "))
if numYour <= num:
    print("Różnica równa jest: " + str(num - numYour))
else:
    print("Podwójna różnica równa jest: " + str((numYour - num) * 2))