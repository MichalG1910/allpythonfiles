def example(x):
    if x > 0:
        return True
    elif x< 0:
        return False
    else:
        pass

a = example(3)
b = example(-3)
c = example(0)

print(f"a:{a}, b:{b}, c:{c}")