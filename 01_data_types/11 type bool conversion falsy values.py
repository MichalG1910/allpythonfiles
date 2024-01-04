
# falsy values czyli wartości które dają false przy konwersji na boolean

print(bool()) # False
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(())) # False                 pusta lista
print(bool([])) # False                 pusta krotka
print(bool({})) # False                 pusty zbiór
print(bool("")) # False                 pusty łańcuch znaków
print(bool(None)) # False

print(bool(True)) # True
print(bool(10)) # True                  konwersja liczby rzeczywistej/całkowitej - musi być różna od zera aby było true
print(bool(-10)) # True
print(bool(-12.345)) # True             
print(bool((1,2,3))) # True             konwersja listy, krotki, zbioru na boolean - musi zawierać conajmniej jeden
print(bool([0])) # True                 element, aby było True
print(bool({0})) # True
print(bool("z")) # True

