
import time
import random
print(" ")
print("Rzut monetą.Orzeł czy Reszka???")
print(" ")
playerName = input("Podaj imię gracza: ")
player = 0
computer = 0
while True:
    
    possibilities = ["orzeł", "reszka"]
    playerChoice = (input("Co wybierasz?" + str(possibilities) + ", exit by wyjść: " ))

    if playerChoice == "exit": break
    
    if not playerChoice in possibilities:
        print("Błedne wprowadzenie, spróbuj jeszcze raz")
        continue
    

    randomChoice = random.choice(["orzeł", "reszka"])
    num = 3
    while num > 0:
        print(num)
        time.sleep(1)
        num -= 1
    else:
        print("wylosowano: " + randomChoice )
        print(" ")
        if randomChoice == playerChoice:
            player += 1
        else:
            computer += 1

        print("Wynik: "  )
        print(str(playerName) + ": " + str(player))
        print("Komputer: " + str(computer))    
        print(" ")