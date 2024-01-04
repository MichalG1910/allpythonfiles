def number_generator(end):
    n = 1
    while n < end:
        yield n
        n += 1

values = number_generator(100)
for v in values:
    print(v)