from sfml import sf
from klasa04kolko_krzyzyk import Board
import os

while True:

    if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE): 
        break

    window = sf.RenderWindow(sf.VideoMode(600,680),"KÓŁKO I KRZYŻYK") # definiujemy naasze obiekt okno do gry (nasza plansza)

    #png - pobieramy tekstury do wyświetlenia na naszej planszy
    textureX = sf.Texture.from_file("./x.png") # pobieramy tekstury z pliku (sf.Texture.from_file)
    textureO = sf.Texture.from_file("./o.png")
    textureS = sf.Texture.from_file("./skull.png")

    arrayX = [] # tworzymy tablicę dla naszego obiektu textureX (dla naszego X). Bedzie to lista 9 argumentów
    for i in range(9): # pętla przejdzie 9 razy, co pozwoli nam wypełnić naszą tablicę(listę) 9 argumentami 
        sprite = sf.Sprite(textureX) # metoda sprite tworzy teksturę z np. naszego obiektu zaiportowanego z pliku(textureX)
        arrayX.append(sprite) # dodajemy nasz obiekt sprite z teksturą do naszej tablicy(listy)

    arrayO  = []
    for j in range(9):
        sprite = sf.Sprite(textureO) 
        arrayO.append(sprite)
    arrayS = []
    for s in range(9):
        sprite = sf.Sprite(textureS) 
        arrayS.append(sprite)

    # Board 
    objectBoard = Board("X") # tworzymy obiekt z naszej klasy Board z klasa04kolko_krzyzyk.py (self.board, self.player, self.win)

    mousePosition = sf.Vector2(-1,-1) # uruchamiamy obsługę myszki, nadajemy jej pozycję poza naszą tablicą (-1,-1)(dla bezpieczeństwa)

    while window.is_open: # tworzymy pętle while window.is_open (= True). Petla będzie działała, dopóki nie wywołamy odpowiedniej komendy kończącej
        
        window.clear(sf.Color(180,180,180)) # czyścimy nasze okno do gry i definiujemy jego kolor z palety kolorów. window.clear(sf.Color.WHITE) - biały

        for event in window.events:
            pass

        # reset, exit
        if sf.Keyboard.is_key_pressed(sf.Keyboard.R): # Reset naszej gry
            window.close()
        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE): # exit -JEŻELI(if)- Keybord.is_key_pressed()- przycisk klawiatury zostanie wciśnięty (Keybord.ESCAPE- przycisk escape)
            break                                          # -TO- zamykamy nasze okno i jednocześnie naszą grę
            
        
        board = objectBoard.return_board() # tworzymy zmienną board, która będzie zwracała naszą planszę (zmienna objectBoard). def return_board --> self.board (z klasy Board)
        
        # obsługa myszki
        if sf.Mouse.is_button_pressed(sf.Mouse.LEFT): # # -JEŻELI(if)- Mouse.is_button_pressed(sf.Mouse.LEFT)-  lewy przycisk myszy zostanie wciśnięty 
            mousePosition = sf.Mouse.get_position() # -TO- weź pozycję myszy 
        
        xmousePosition = mousePosition - window.position # window.position (lewy górny róg naszego okna) Jeśli okno ma wsp. x=400, y=400, to kliknięcie myszą np. w x=460, y=460 da 
                                                        # nam xmousePosition x=60, y=60. (Lewy górny róg ekranu monitora ma współrzędne x=0, y=0 i od niego ustala sie współrzędne)
        if xmousePosition.x > 0 and xmousePosition.y > 35: # sprawdzamy, czy nasze kliknięcie nie było na lewo od naszej planszy lub nad naszą planszą do gry. Prawą krawędź i dolną krawędź
                                                        # sprawdzą instrukcje poniżej. Jeśli kliknięcie odbędzie się w oknie naszej gry, to zostanie umieszczone X lub O
            
            if xmousePosition.x < 200: 
                if xmousePosition.y < 235:
                    objectBoard.put_to_board(1, 1)
                elif xmousePosition.y < 435:
                    objectBoard.put_to_board(1, 2)
                elif xmousePosition.y < 635:
                    objectBoard.put_to_board(1, 3)
            
            elif xmousePosition.x < 400:
                if xmousePosition.y < 235:
                    objectBoard.put_to_board(2, 1)
                elif xmousePosition.y < 435:
                    objectBoard.put_to_board(2, 2)
                elif xmousePosition.y < 635:
                    objectBoard.put_to_board(2, 3)

            elif xmousePosition.x < 600:
                if xmousePosition.y < 235:
                    objectBoard.put_to_board(3, 1)
                elif xmousePosition.y < 435:
                    objectBoard.put_to_board(3, 2)
                elif xmousePosition.y < 635:
                    objectBoard.put_to_board(3, 3)
        # instrukcje powyżej sprawdzają i umieszczają w miejscu kliknięcia myszą odpowiednio X lub O. Korzystamy z put_to_board (z naszego pliku z klasą)
        # np. mousePosition.x < 200: , xmousePosition.y < 200: --> objectBoard.put_to_board(1, 1). Odpowiedni znak zostanie umieszczony na self.board[x-1][y-1],
        # czyli pod indeksem [0][0] naszej tablicy: self.board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]
                


        
        #body game
        rectangle1 = sf.RectangleShape() # definiujemy obiekt prostokąt 
        rectangle1.size = (600, 0) # nadajemy mu rozmiar (600, 0). Wysokość 0, szerokość 600
        rectangle1.outline_color = sf.Color.BLACK # nadajemy mu kolor czarny
        rectangle1.outline_thickness = 2 # nadajemy mu grubość 2 
        rectangle1.position = (0, 200) # ustalamy jego pozycję (oś x = 0, oś y = 200)

        rectangle2 = sf.RectangleShape()
        rectangle2.size = (600, 0)
        rectangle2.outline_color = sf.Color.BLACK
        rectangle2.outline_thickness = 2
        rectangle2.position = (0, 400)

        rectangle3 = sf.RectangleShape()
        rectangle3.size = (0, 600)
        rectangle3.outline_color = sf.Color.BLACK
        rectangle3.outline_thickness = 2
        rectangle3.position = (200, 0)

        rectangle4 = sf.RectangleShape()
        rectangle4.size = (0, 600)
        rectangle4.outline_color = sf.Color.BLACK
        rectangle4.outline_thickness = 2
        rectangle4.position = (400, 0)

        rectangle5 = sf.RectangleShape()
        rectangle5.size = (600, 80)
        rectangle5.outline_color = sf.Color.WHITE
        #rectangle4.outline_thickness = 2
        rectangle5.position = (0, 600)

        rectangleH = sf.RectangleShape()
        rectangleH.size = (580, 0)
        rectangleH.outline_color = sf.Color.WHITE
        rectangleH.outline_thickness = 12
        
        

        window.draw(rectangle1) # rysujemy(umieszczamy) nasz obiekt w naszym oknie (na naszej planszy do gry)
        window.draw(rectangle2)
        window.draw(rectangle3)
        window.draw(rectangle4)
        window.draw(rectangle5)

        drawarray = [] # drukujemy naszą planszę startową, czyli przypisujemy odpowiednie tekstury array do odpowiedniego miejsca na naszej planszy
        for x in range(3): # [0,1,2]
            for y in range(3): # takie skożystanie z 2 pętli for stworzy nam tablicę 3x3, czyli z 9 pozycjami
                if board[x][y] == ".": # board--> objectBoard --> self.board z naszej klasy Board w klasa04kolko_krzyzyk.py --> [[".", ".", "."],[".", ".", "."],[".", ".", "."]]
                # jeśli obiekt o współrzędnych board[x][y] == ".", to do naszej tablicy drawarray zostanie dodana tekstura arrayS
                    arrayS[3 * x + y].position = sf.Vector2(200 * x, 200 * y) # pozycjonujemy nasz  arrayS[indeks]na podstawie współrzędnych [x][y]
                    drawarray.append(arrayS[3 * x + y]) # i dodajemy do drawarray, arrayS = [textureS, textureS, textureS, textureS, textureS, textureS, textureS, textureS, textureS]
                    # board[1][2]=="." --> arrayS[5].position = sf.Vector2(200, 400) --> drawarray.append(arrayS[5]) --> dodajemy arrayS[5] do listy drawarray

                # czynność powtarzamy dla X i O

                elif board[x][y] == "X":
                    arrayX[3 * x + y].position = sf.Vector2(200 * x, 200 * y) 
                    drawarray.append(arrayX[3 * x + y])
            
                else:
                    arrayO[3 * x + y].position = sf.Vector2(200 * x, 200 * y) 
                    drawarray.append(arrayO[3 * x + y])
        # na koniec działania otrzymujemy nasza tablicę(listę) z textureX, textureO, textureS. 
        # na przykład: drawarray = [textureX, textureX, textureO, textureS,textureS, textureO, textureS, textureS, textureOS]

        for elementToDraw in range(9): # teraz tworzymy pętle, która umiesści nasze tekstury zawarte w naszej liście drawarray
            window.draw(drawarray[elementToDraw]) # wyświetla na naszym oknie window odpowiednią teksturę w odpowiednim miejscu

        #window.display() # wyświetlamy nasze okno

        mousePosition.x = -1 # po każdym kliknięciu myszy ustawiamy ją spowrotem na współrzędnych (-1,-1)
        mousePosition.y = -1

        # końcowy wydruk w oknie (definicja wyświetlenia tekstu)
        def comunicat(tekst):
            font = sf.Font.from_file("aakar-medium.ttf")
            text = sf.Text(tekst)
            text.font = font
            text.character_size = 30
            text.style = sf.Text.BOLD
            text.position = (10, 602)
            text.color = sf.Color.BLACK
            window.draw(text)

        # sprawdzenie warunków wygranej

        if objectBoard.check_if_draw():
            comunicat('-----------------REMIS----------------\n(R)eset                       (ESC)ape')
            
        if objectBoard.check_if_win():
            if objectBoard.x == None:
                if objectBoard.y == 0:
                    rectangleH.position = (10, 100)
                elif objectBoard.y == 1:
                    rectangleH.position = (10, 300)
                else:
                    rectangleH.position = (10, 500)
            
            if objectBoard.y == None:
                if objectBoard.x == 0:
                    rectangleH.position = (100, 10)
                    rectangleH.rotation = 90
                elif objectBoard.x == 1:
                    rectangleH.position = (300, 10)
                    rectangleH.rotation = 90
                else:
                    rectangleH.position = (500, 10)
                    rectangleH.rotation = 90

            if objectBoard.slant != None:
                if objectBoard.slant == "001122":
                    rectangleH.position = (10, 10)
                    rectangleH.rotation = 45
                    rectangleH.size = (820, 0)
                else:
                    rectangleH.position = (10, 590)
                    rectangleH.rotation = -45
                    rectangleH.size = (820, 0)

                    
            window.draw(rectangleH)


            if objectBoard.get_player() == "O":
                comunicat('---------------WYGRAL X---------------\n(R)eset                       (ESC)ape')
                
            else:
                comunicat('---------------WYGRAL O---------------\n(R)eset                       (ESC)ape')

        window.display()
        




    
    