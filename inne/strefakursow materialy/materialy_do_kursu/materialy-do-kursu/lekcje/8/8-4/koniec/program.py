class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to_new_coords(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(3, 5)
print(p1.x, p1.y)
p1.move_to_new_coords(12, 4)
print(p1.x, p1.y)
