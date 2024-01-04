def add(a :int = 0, b : int = 0) -> str:
    return str(a+b)

print(add(10,10))

print(add.__name__)
print(add)

def function_generator(nochange, ifUpper):
    def repeatText(text, how_many_repeat = 1):
        return text * how_many_repeat
    def repeatUpper(text :str, how_many_repeat = 1):
        return text.upper() * how_many_repeat
    def repeatLower(text :str, how_many_repeat = 1):
        return text.lower() * how_many_repeat

    if nochange:
        return repeatText
    else:
        if ifUpper:
            return repeatUpper
        else:
            return repeatLower

functionUpper = function_generator(False,True)
print(functionUpper("Piotr Koska",2))

functionLower = function_generator(False,False)
print(functionLower("Piotr Koska",2))