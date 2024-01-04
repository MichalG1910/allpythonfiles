from klasa02Carhermetyzacja import Car

value = float(input("Provide the amount of fluids: "))
unit = input("L for liters or G for galons: ")
myCar = Car()
myCar.setTank(value, unit)

while True:
    choice = int(input("0 - liters <--> galons, 1 - change tank size, 2 - exit: "))
    if choice == 2: break
    elif choice == 0:
        unit = input("L for liters or G for galons: ")
        print(myCar.getTank(unit))
    elif choice == 1:
        value = float(input("Provide the amount of fluids: "))
        unit = input("L for liters or G for galons: ")
        myCar.setTank(value, unit)
    else:
        pass

    # 1. Podajemy: value, unit
    # 2. tworzymy obiekt myCar
    # 3. wykonujemy funkcję setTank. 
    #   4. Jeżeli unit = L, wtedy nasza ilośc paliwa jest w litrach
    #      więc wykonuje się instrukcja [if  funkcji SetTank] i self.tank = liquid (nic nie przeliczamy)
    #   4. jeżeli unit = G, czyli podaliśmy naszą ilość paliwa w galonach, to wykonuje się 
    #      instrukcja [elif funkcji SetTank] i self.tank = liquid / 0.26417 (nasz self tank w pamięci zostaje 
    #      przeliczony na litry)
    # 5. zaczyna się funkcja while True
    #   6. choice "0" - przeliczenie z litrów na galony i odwrotnie
    #       7. wykonujemy funkcję getTank (pamiętamy, że nasz set.tank zawsze przechowywany jest w litrach patzr pkt.4)
    #           8. unit wybieramy "L" - wtedy funkcja getTank wykona instrukcję if  i zwróci self.tank 
    #              (niezalężnie od tego, czy w pkt.4 wybraliśmy "L" cz "G")
    #           8. unit wybieramy "G" - wtedy funkcja getTank wykona instrukcję elif  i zwróci self.tank * 0.26417
    #              (niezalężnie od tego, czy w pkt.4 wybraliśmy "L" cz "G") (żeby podać ilość paliwa w galonach, musimy
    #              nasz self.tank pomnożyć 0.26417, ponieważ self.tank jest przechowywany w pamięci zawsze w litrach)  
    #   9. choice "1" = zauważ, że jest to kopia instrukcji z początku skryptu, z przed funkcji while. Po tym wyborze
    #      rozpoczniemy przeliczanie dla nowej ilości paliwa
    #   10. choice "2" - zakończenie funkcji while i całego skryptu                
    #           



