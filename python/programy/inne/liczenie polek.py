print("""      _______________________________________
            |  _______________________________________
            |  |
            |  |
            |  |
            |  | odległość między pólkami
            |  |
            |  |
            |  _______________________________________
wysokość    |  _______________________________________
            |  |
            |  |
            |  |
            |  |
            |  |
            |  |
            |  _______________________________________
            |  _______________________________________
""")
reset = True
print("Liczysz pólki bez pólki sufitowej i podłogowej (półki wewnętrzne)")
print(" ")

while True:
    
    wysokość = float(input("Podaj wysokość szafki(mm): " ))
    ilośćPółek = int(input("podaj ilość półek: "))
    grubośćPłyty = float(input("Podaj grubość płyty meblowej(mm): "))
    

    odległośćMP = (wysokość - grubośćPłyty) / (ilośćPółek + 1) - grubośćPłyty
    odległośćSrodekPólki = (wysokość - grubośćPłyty) / (ilośćPółek + 1)
    print(" ")
    print("odległość miedzy pólkami od krawędzi półek = " + str(odległośćMP) + " mm")
    print("odległość miedzy pólkami od środka półek = " + str(odległośćSrodekPólki) + " mm")
    print(" ")

    if reset == True:
        zakoncz = str(input("Wpisz exit aby zakończyć lub cokolwiek innego aby liczyć jeszcze raz: " ))
        if zakoncz == "exit": break



    