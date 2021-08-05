set1 = set()

set2 = {"Mon", "Tue", "Thu", "Wed"}
print(set2)

set3 = {1, 2, 3, 5, 4}
print(set3)  # print(set3)  #

set4 = {1.2, 3.14, 5.5}
print(set4)

lst = [12, 1.3, 56, "EVO"]
print(type(lst))  # <class 'list'>
set6 = set(lst)
print("set6:", set6)  # set6: {56, 1.3, 12, 'EVO'}
print(type(set6))  # <class 'set'>

tup2 = (1, 1.5, "tup", 'T', 2, 3, 5, 6)
print(tup2)
set7 = set(tup2)
print(set7)

# {1, 1.5, "tup", 'T', 2, 3, 5, 6}

for s in set7:
    print(s)

name = "Python on process"
set8 = set(name)
print(set8)  # set จะไม่เก็บค่าซ้ำ

set9 = {2, 3, 4, 5, 1}  # เรียงแค่เลข
for s in set9:
    print(s, end=' ')

set2 = {"Mon", "Tue", "Thu", "Wed"}
set2.add("Fri")
print(set2)

set3.add(6)
print(set3)

set2.discard("Mon")
print(set2)

set3.discard(2)

setX = {1, 2, 3, 4, 5}
setY = {3, 4, 5, 6, 7}

print(setX | setY)  # หรือ   > {1, 2, 3, 4, 5, 6, 7}
print(setX & setY)  # และ   > {3, 4, 5}
print(setX - setY)  # เอา X ไม่เอา Y     {1, 2}
print(setY - setX)  # เอา Y ไม่เอา X     {6, 7}
print(setX ^ setY)  # ส่วนกลับของ setX & setY  เหมือนเอา หรือมาลบกับและ {1, 2, 6, 7}

print(3 in setX)  # True
print(6 in setX)  # False
print(6 not in setX)  # True
