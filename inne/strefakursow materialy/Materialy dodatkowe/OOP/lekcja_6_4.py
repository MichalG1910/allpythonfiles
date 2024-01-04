class Board:

    def __init__(self, player):
        self.board = [[".",".","."],[".",".","."],[".",".","."]]
        self.player = player
        self.win = False

    def check_if_win(self):
        for x in range(0,3):
            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "X" or self.board[x][2] == "O"):
                self.win = True
                return True

        for y in range(0,3):
            if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and (self.board[2][y] == "X" or self.board[2][y] == "O"):
                self.win = True
                return True

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "X" or self.board[2][2] == "O"):
            self.win = True
            return True

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and (self.board[2][0] == "X" or self.board[2][0] == "O"):
            self.win = True
            return True

        return False

    def check_if_draw(self):
        if not self.check_if_win():
            for row in self.board:
                for element in row:
                    if element == ".":
                        return False
            return True
        else:
            return False

    def show_board(self):
        print("  1 2 3")
        numberRow = 1
        for row in self.board:
            print(numberRow, end = " ")
            for element in row:
                print(element, end = " ")
            print()
            numberRow += 1

    def check_if_free(self, x, y):
        return self.board[x-1][y-1] == "."

    def change_player(self):
        if self.player == "O":
            self.player = "X"
        else:
            self.player = "O"

    def put_to_board(self, x, y):
        if self.check_if_free(x, y):
            self.board[x-1][y-1] = self.player
            self.change_player()

    def get_player(self):
        return self.player

    def return_board(self):
        return self.board




