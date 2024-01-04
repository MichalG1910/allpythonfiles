import lekcja_6_4 as Board

print("Zacznijmy gre:")
player = input("Kto ma zacząć X czy O: ")

board = Board.Board(player.upper())

while (not board.check_if_win()) and (not board.check_if_draw()):
    board.show_board()
    x, y = [int(x) for x in input("Podaj wspołżedne pola na którym chcesz postawić X badz O: ").split()]
    board.put_to_board(x, y)

board.show_board()
print()
if board.check_if_win():
    if board.get_player() == "X":
        print("Wygral O")
    else:
        print("Wygral X")
else:
    print("Remis nikt nie wygral.")
