lst1 = []

lst2 = [1, 2.5, "lst", 'B']
lst3 = [3, ['A', "str"]]
lst2.append(5)  # lst2 = [1, 2.5, "lst", 'B', 5]
lst4 = [2]

print(lst3[1][0])  # 'A'
print(lst2[0])

print(lst2[0] + lst3[0])  # 4 = 1 + 3

print(lst2 + lst3)  # [1, 2.5, 'lst', 'B', 3, ['A', 'str']]

# lst4 = [2]
print(lst4 * 2)  # [2,2]
print(lst4[0] * 2)  # [4]

# lst2 = [1, 2.5, "lst", 'B']
print(2.5 in lst2)  # True

print(len(lst2))  # 4  # Function

# [1, 2.5, 'lst', 'B']

lst2.append(6)  # Methods
print(lst2)  # [1, 2.5, 'lst', 'B', 6]
print(len(lst2))  # 5

lst2.insert(1, '4')  # เพิ่ม '4' ในตำแหน่งที่ 1
print(lst2)  # [1, '4', 2.5, 'lst', 'B', 6]   len = 6

lst2.remove(2.5)  # [1, '4', 'lst', 'B', 6]
print(lst2)

# lst3 = [3, ['A', "str"]]
del lst3[1][0]  # delete 'A' in lst3
print(lst3)  # [3, ['str']]  [3, ['str']]

lst = [2, 5, 1, 6, 7, 9, 10, 4]
print(sum(lst))  # Function sum

Sum = 0
for i in lst:
    Sum += i
print(Sum)
