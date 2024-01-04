class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(3, 5)
p2 = Point()
print(p1.x, p1.y)
print(p2.x, p2.y)