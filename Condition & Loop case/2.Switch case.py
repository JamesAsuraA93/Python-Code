"""

def function_name(argument):
    [statement]
    return [value]
    
def b(x):
    return 1+x

function_name = lambda (argument) [value] : (return) [value]


b = lambda x : result = 1 + x : result

function ไม่มี . มีแต่ name(variable)

methods มี . เช่น   variable.name()
    
"""


def say():
    return "error"


def switch(choice):
    eiei = {0: "zero",
            1: "one",
            2: "two",
            3: "three"}
    return eiei.get(choice, say())


print(switch(4))


def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")


print(week(6))  # Saturday


def detect(num):
    num = num % 2

    swch = {
        0: "คู่"
    }
    print(swch.get(num, "คี่"))


detect(3)


def zero():
    return 'zero'


def one():
    return 'one'


def indirect1(i):
    switcher = {
        0: zero,
        1: one,
        2: lambda: 'two'
    }

    func = switcher.get(i)
    # func = lambda 2:'two'
    return func()


print(indirect1(2))


def indirect2(i):
    switcher = {
        0: zero,
        1: one,
        2: lambda: 'two'
    }

    func = switcher.get(i, lambda: 'Invalid')
    return func()


print(indirect2(4))
