class Point:
    points_counter = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points_counter += 1

    def move_to_new_coords(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(3, 5)
p2 = Point(4, 9)
print(Point.points_counter)
print(p1.points_counter)