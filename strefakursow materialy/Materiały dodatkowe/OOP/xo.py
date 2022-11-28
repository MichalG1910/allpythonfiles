from sfml import sf
from lekcja_6_4 import Board

window = sf.RenderWindow(sf.VideoMode(600,600),"Tic Tak Toe")

#png
textureX = sf.Texture.from_file("./x.png")
textureO = sf.Texture.from_file("./o.png")
textureS = sf.Texture.from_file("./skull.png")

arrayX = []
for i in range(9):
    sprite = sf.Sprite(textureX)
    arrayX.append(sprite)

arrayO = []
for j in range(9):
    sprite = sf.Sprite(textureO)
    arrayO.append(sprite)

arrayS = []
for s in range(9):
    sprite = sf.Sprite(textureS)
    arrayS.append(sprite)

#Board

objectBoard = Board("X")

mousePosition = sf.Vector2(-1,-1)

while window.is_open:
    window.clear(sf.Color.WHITE)

    for event in window.events:
        pass

    #exit
    if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
        window.close()

    board = objectBoard.return_board()

    if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
        mousePosition = sf.Mouse.get_position()
    xmousePosition = mousePosition - window.position

    if xmousePosition.x > 0 and xmousePosition.y >0:
        if xmousePosition.x < 200:
            if xmousePosition.y < 200:
                objectBoard.put_to_board(1,1)
            elif xmousePosition.y < 400:
                objectBoard.put_to_board(1,2)
            else:
                objectBoard.put_to_board(1,3)
        elif xmousePosition.x < 400:
            if xmousePosition.y < 200:
                objectBoard.put_to_board(2,1)
            elif xmousePosition.y < 400:
                objectBoard.put_to_board(2,2)
            else:
                objectBoard.put_to_board(2,3)
        else:
            if xmousePosition.y < 200:
                objectBoard.put_to_board(3,1)
            elif xmousePosition.y < 400:
                objectBoard.put_to_board(3,2)
            else:
                objectBoard.put_to_board(3,3)

    rectangle1 = sf.RectangleShape()
    rectangle1.size = (600, 0)
    rectangle1.outline_color = sf.Color.BLACK
    rectangle1.outline_thickness = 2
    rectangle1.position = (0, 200)

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

    window.draw(rectangle1)
    window.draw(rectangle2)
    window.draw(rectangle3)
    window.draw(rectangle4)

    drawarray = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == ".":
                arrayS[3 * x + y].position = sf.Vector2(200 * x, 200 * y)
                drawarray.append(arrayS[3 * x + y])
            elif board[x][y] == "X":
                arrayX[3 * x + y].position = sf.Vector2(200 * x, 200 * y)
                drawarray.append(arrayX[3 * x + y])
            else:
                arrayO[3 * x + y].position = sf.Vector2(200 * x, 200 * y)
                drawarray.append(arrayO[3 * x + y])

    for elementToDraw in range(9):
        window.draw(drawarray[elementToDraw])


    window.display()
    mousePosition.x = -1
    mousePosition.y = -1

    if objectBoard.check_if_win() or objectBoard.check_if_draw():
        break

if objectBoard.check_if_draw():
    print("REMIS")
else:
    if objectBoard.get_player() == 'O':
        print("Wygral X")
    else:
        print("Wygral O")

