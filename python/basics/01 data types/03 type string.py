
str = "Hello World!"
print(str)
print(len(str)) # 12 - len - zwraca liczbę znaków (numerowane od 1)
print(type(str)) # <class 'str'>
print(str[0]) # H - wyciągnięcie znaku z ciągu znaków (numerowanie od 0. Zero to pierwszy znak)
print(str[0:5]) # Hello - wyciągnięcie znaków od 1 do 4 , 5 oznacza na który znaku ma zakończyć i jej nie pokaże

print(str[len(str) - 1])# ! - taki zapis umożliwia podanie ostatniego znaku z ciągu znaków

print(str * 4)# powtórzy ciąg zanaków 4 razy
strx3 = str * 3
print(strx3)
str2 = str + " and hello again!" # Hello World! and hello again!
print(str2)

print(str2[6:])# World! and hello again! - pokaże z ciągu znaków znaki od 6 do ostatniego
print(str2[::3])# HlWl deogn - pokaże co 3 literę z ciągu znaków z uwzględnieniem 1 litery

multiLine = """Pierwsza linia
Druga linia
Trzecia linia
""" # potrójny cudzysłów otwiera wieloliniowy łańcuch znaków
print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia \t \"linia\"\\" # \ backslash - znak specjalny tzw ucieczki
# np \n - następna linia    \t - tabulator  \" - dodatkowy cudzysłów w łańcuchu znaków"
# \\ - dodatkowy backslash w łańcuchu znaków
print(multiLine2)