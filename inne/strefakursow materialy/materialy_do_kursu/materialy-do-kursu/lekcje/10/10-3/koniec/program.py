try:
    print('Probujemy podzielic')
    a = 2 / 0
    print(a)
except ZeroDivisionError:
    print('Blad! - dzielenie przez zero!')