def my_decorator(fn):
    def wrapper():
        print('Poczatek odliczania')
        fn()
        print('Koniec odliczania')
    return wrapper

@my_decorator
def get_5_values():
    for v in range(1,6):
        print(v)

# get_5_values_decorated = my_decorator(get_5_values)
# get_5_values_decorated()
get_5_values()