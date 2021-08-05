"""def biggest(a,b):
    if a > b:
        return a
    else:
        return b

def smallest(a,b):
    if a < b:
        return a
    else:
        return b

def my_max_mid_min(a,b,c):
    mx = biggest(biggest(a,b),c)
    mn = smallest(smallest(a,b),c)
    md = (a+b+c) - (mx+mn)
    print(f"max = {mx} mid = {md}min = {mn}")

my_max_mid_min(1,2,3)
"""
"""
n_lst = []
l_lst = int(input())

for i in range(l_lst):
    num = int(input())
    n_lst.append(num)

lst = n_lst
ln = len(lst) - 1

for i in range(0,ln):

    for j in range(0,len(lst) -1):

        if lst[j] < lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp

    ln -= 1

print(lst)
"""

# Sorting Bubbles

number = []
for i in range(0,3):
    x = int(input())
    number.append(x)
print(number)
length_numlist = len(number)
tmp = len(number)
for i in range(0,length_numlist):

    for j in range(0,tmp -1):

        if number[j] < number[j+1]:
            temp = number[j]
            number[j] = number[j + 1]
            number[j + 1] = temp

    tmp -= 1

print(number)


# [1,2,3]
# [2,1,3]
# [2,3,1]
# [3,2,1]
