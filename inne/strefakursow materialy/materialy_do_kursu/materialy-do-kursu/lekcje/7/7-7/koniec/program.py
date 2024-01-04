x = 1

def fn():
    global x
    x += 1
    y = 3
    print(x, y)

fn()
print(x)