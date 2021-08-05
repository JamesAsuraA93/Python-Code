def test1(a, b):
    c = a // b
    e = a ** b
    d = a + b
    return c


result = test1(5, 2)
print(result)


def test2(lst):
    a, b = lst[0], lst[1]  # a, b = 5, 2 > a = 5 :  b = 2
    tmp = [0, 0, 0]
    tmp[0] = a // b
    tmp[1] = a ** b
    tmp[2] = a + b
    # tmp = [0, 0, 0]
    # tmp = [a // b , a ** b, a + b]
    return tmp


data = [5, 2]

result = test2(data)  # Inst

print(result[::])
print(result[1:])
print(result[0])
print(result[1])
print(result[2])
