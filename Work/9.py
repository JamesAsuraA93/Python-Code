"""def nearest_odd(x):
    x = int(x)
    if x%2==0:
        print(x+1)
    else:
        print(x)

nearest_odd(4.2)
"""

"""
def nearest_odd(x):
    x_string = str(x)
    if '.' in x_string:
        ind = x_string.index('.')
        new_string = x_string[ind - 1]
        if int(new_string) % 2 != 0:
            print(int(new_string))
        else:
            print(int(new_string) + 1)
    else:
        if x % 2 == 0:
            print(x+1)
        else:
            print(x)

nearest_odd(3)"""
