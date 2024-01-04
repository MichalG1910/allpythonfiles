from xmlrpc.client import boolean



# isinstance(argument, TYP) - funkcja sprawdza, czy nasz szukany argument jest danym TYPEM

print(isinstance(10, int)) # True
print(isinstance(10.9, int)) # False
print(isinstance(2 + 4, int)) #True 
print(isinstance("str", int)) # False
print(isinstance(5.5, (int, float))) # True
print(isinstance(5, (int, float))) # True
print(isinstance(True, bool)) # True
