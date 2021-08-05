"""for i in range(5):  # 0,1,2,3,4
    print(i, end=" ")  # 0 1 2 3 4
else:
    print(" success")  # 0 1 2 3 4  success

primes = [2, 3, 5, 7]
classic_num = [0,1,2,3,4]
n = 0
legth = len(primes) # 4
for prime in range(0,legth):
    print(primes[prime], end = " ")
"""

for ch in "Hello World":
    print(ch, end=' ')
else:
    print("")

rows = 5
# rows = 0 cols = 0    x,y = 0,0
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end='')
    print("")

cols = 5
next = 5
for m in range(0, cols):
    for n in range(0, next):
        if m >= n:
            print("*", end="")
    print("")

square = 0
number = 1

while number < 10:  # True  จะทำให้ statement
    square = number ** 2
    print(square)
    number += 1

print("")

x = 0
j = 8
while x < 10:
    while j > 5:
        print("Hello J")
        j -= 1
    print(x)
    x += 2
