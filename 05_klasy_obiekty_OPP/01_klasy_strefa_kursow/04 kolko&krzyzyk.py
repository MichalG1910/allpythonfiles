import klasa04kolko_krzyzyk as Bo # importujemy moduł z pliku i nadajemy mu skróconą nazwę Bo

print("Zacznijmy grę!")
player = input("Kto ma zaczynać, X cz O: ") # określamy zawodnika( X lub O)

board = Bo.Board(player.upper()) # tworzymy obiekt na klasie Board (__init__ wymusza zmienną, w naszym przypadku będzie to zmienna z input powyżej)

while (not board.check_if_win()) and (not board.check_if_draw()): # pętla while jeśli (check_if_win nie jest True) i (check_if_draw nie jest True)
    # nasza petla while będzie działać, aż warunek wygranej (board.check_if_win) lub remisu (check_if_draw) nie zostanie spełniony
    board.show_board() # wyświetla naszą aktualną tablicę do gry po każdym przejściu petli while
    x, y = [int(x) for x in input("Podaj współrzędne pola na którym chcesz postawić X albo O: ").split()] # wprowadzenie współrzednych X lub O
    board.put_to_board(x, y) # umieszczenie X lub Y na naszej tablicy do gry
board.show_board() # wyświetlenie tablicy do gry po zakończeniu pętli (koniec gry)


print()
if board.check_if_win():  # jeżeli check_if_win = True to sprawdzmy kolejne if
    if board.get_player() == "X": # bierzemy aktualnego gracza(get_player), który ma wykonać ruch i sprawdzamy czy to X - jeśli tak to
            print("Wygrał O\n") # wygrał gracz O
    else: # jeśli nie, to 
        print("Wygrał X\n") # wygrał gracz X
else: # jeśli board.check_if_win() = False, to mamy remis
    print("Remis nikt nie wygrał\n") 

# po wprowadzenia przez gracza X lub O kończącego grę(spełnimy warunek check_if_win), to funkcja check_if_win zdąży jeszcze zmienić 
# zmienną player na drugiego gracza (tego co przegrał). Dlatego jeśli board.get_player() == "X" to wygrywa gracz O, i na odwrót  