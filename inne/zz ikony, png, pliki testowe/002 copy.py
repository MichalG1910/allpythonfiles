a = int(input('Liczba:'))
print(type(a))
bin = bin(a)[2:]
print('Binarne:', bin)
oct = oct(a)[2:]
print('Osemkowe:', oct)
hex = hex(a)[2:]
print('szesnastkowy:', hex, "            szesnastkowy - heksadecymalny")

print(int(bin,2))
print(int(oct,8))
print(int(hex,16))