from re import A


class Board:
    def __init__(self, player):
            # indeksy | 00 , 01 , 02  | 10 , 11 , 12  | 20 , 21 , 22
        self.board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]] # nasza tablica do gry. Są to 3 listy zagnieżdżone w jednej liście
        self.player = player
        self.win = False # początkowo ustawione na False

    def check_if_win(self): # definicja sprawdzenia warunków wygranej
        for x in range(0,3): # iteracja x z listy (0,1,2)
            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "X" or self.board[x][2] == "O"):
                self.win = True # jeżeli instrukcja if zostanie spelniona, zmienia się wartość logiczna self.win na True
                return True # po spełnieniu warunku if funkcja check_if_win zwróci True
                # iterujemy x z listy (0,1,2), w zmiennej self.board[x][0] podstawiamy nasz ziterowany x. Każde przejście pętli for sprawdza jeden rząd 
                # rząd (na osi X)naszej planszy do gry. Jeżeli w którymś z rzędów będą same X lub same O, if zostanie spełniona i nasza funkcja da True
                # if: 00 = 01 and[i] 01 = 02 and 02 = (X or[lub] O) --> 00=01=02=X lub 00=01=02=O --> return True (zapis 1 rząd)
        
        for y in range(0,3):        
            if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and (self.board[2][y] == "X" or self.board[2][y] == "O"):
                self.win = True
                return True
                # j.w, tylko sprawdzamy kolumnę (oś Y): 
                # if: 00 = 10 and[i] 10 = 20 and 20 = (X or[lub] O) --> 00=10=20=X lub 00=10=20 --> return True (zapis 1 kolumna)
        
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "X" or self.board[2][2] == "O"):
            self.win = True
            return True 
            # 00=11=22=X lub 00=11=22 --> return True (zapis 1 skos)   
        
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and (self.board[2][0] == "X" or self.board[2][0] == "O"):
            self.win = True
            return True
            # 02=11=20=X lub 02=11=20 --> return True (zapis 2 skos)
            # 2 instrukcje if powyżej sprawdzają to samo, co dwie pierwsze, jednak robią to dla skosów. Skosy są tylko 2, więc nie używamy pętli for

        return False # False jeżeli żaden if powyżej nie zostanie spełniony

    def check_if_draw(self):
        if not self.check_if_win(): # jeżeli check_if_win nie True - 
            for row in self.board:  # iterujemy po naszej self.board(jest ona listą z trzema listami zagnieżdżonymi w sobie) Row po iteracji to jedna z tych zagnieżdżonych list
                for element in row: # iterujemy po argumentach z listy row
                    if element == ".": # jeżeli w naszej tablicy self.board jest choć jedno puste pole ".", gra się nie zakończyła,
                        return False   # i  funkcja check_if_draw zwracamy False
            return True # jeżeli nie ma  ".", funkcja check_if_draw zwracamy True (mamy remis)
        else: # jeżeli check_if_win nie False - check_if_draw zwracama False( check_if_win to true, więc mamy wygranego)
            return False

    def show_board(self): # funkcja rysuje naszą tablicę do gry
        print("  1 2 3") # numeracja na osi X
        numberRow = 1
        for row in self.board: # iteracja z naszej listy 3 list
            print(numberRow, end = " ") # spowoduje opisanie naszej osi Y (po każdym przejściu for numberRow += 1)(end = " " - spacja po cyfrze dla polepszenia wyglądu tablicy)
            for element in row: # iterujemy po argumentach naszych 3 list ( na początku gry każdy argument = ".")
                print(element, end = " ") # END = " " - POWODUJE, ŻE ITEROWANE ELEMENTY SĄ WYŚWIETLANE W JEDNYM WIERSZU
            print()                       # W STRING MOŻNA WSTAWIĆ DOWOLNY ZNAK, KTORY BEDZIE ODDZIELAŁ ITEROWANE ARGUMENTY
            numberRow += 1

    def check_if_free(self, x, y): # funkcja sprawdza, czy dane pole jest puste self.board[y-1][x-1] == "."
        return self.board[y-1][x-1] == "." # x, y będą wprowadzane z klawiatury, więc trzeba odjąc od nich 1, aby współrzędne odpowiadały indeksowi 
                                           # w naszej liście. Y jako pierwszy indeks aby poprawnie opisać w czasie gry osie (przeanalizuj - to twoja zmiana)

    def change_player(self): # po każdym wprowadzeniu współrzędnych czyli dodaniu X lub O na naszą tablicę, zmienia zawodnika (wprowadzany znak) 
        if self.player == "O": # jeżeli gracz = O
            self.player = "X"  # wtedy funkcja change_player zwróci self.player = "X"
        else:                  # Jeżeli instrukcja if nie spełniona, znaczy że był self.player = "X" i teraz zmienia na self.player = "O"
            self.player = "O"

    def put_to_board(self, x, y): # dodanie naszego X lub O
        if self.check_if_free(x, y): # sprawdza, czy pole puste (patrz opis check_if_free)
            self.board[y-1][x-1] = self.player # wprowadzenie X lub O (self.player równy jest "X" lub "O") - zastąpienie elementu listy "." na X lub O
            self.change_player() # zmiana zawodnika (wprowadzanego znaku X lub O)
    def get_player(self): # po wywołaniu zwraca zawodnika( znak do wprowadzenia X lub O)
        return self.player






        
            



