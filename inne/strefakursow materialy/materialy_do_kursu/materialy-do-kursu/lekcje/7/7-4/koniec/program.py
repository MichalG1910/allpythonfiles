def fn(a, *args, **dict_args):
    print(a)
    for arg in args:
        print(arg)
    for key in dict_args:
        print(dict_args[key])

fn(3, 2, 4, 5, True, 'cx', user='admin', version=1.0, db='sql')