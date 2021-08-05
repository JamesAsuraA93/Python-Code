"""def round_to_int(x):
    str_x = str(x)
    ind = str_x.index('.')
    last_float = str_x[ind+1:]
    num = int(last_float)
    if num >= 5:
        x += 1 - num/10
        last_str = str(x)
        print(int(last_str[:1]))
    else:
        x -= num/10
        last_str = str(x)
        print(int(last_str[:1]))


round_to_int(2.7)"""
"""
def round_to_int(x):
    str_x = str(x)
    ind = str_x.index('.')
    last_float = str_x[ind + 1:]
    num = int(last_float)
    if num >= 5:
        print(int(x+0.5))
    else:
        print(int(x))

"""
"""
def round_to_int(x):
    if x < 0:
        print(int(x - 0.499999999999999999999999999999999999))
    else:
        print(int(x + 0.49999999999999999999999999999999999))

round_to_int(2.5)"""