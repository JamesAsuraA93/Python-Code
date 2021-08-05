# Single Passing
def div(a, b):
    c = a // b
    return c


print(div(5, 1))


# Multi Passing
def Sum(The_lst):
    sum = 0
    for i in The_lst:
        sum += i  # sum เดิมเพิ่มค่า i ใหม่ไปเรื่อย ๆ
    return sum


lst = [2, 5, 1, 6, 7, 9, 10, 4]

print("Sum is ", Sum(lst))
