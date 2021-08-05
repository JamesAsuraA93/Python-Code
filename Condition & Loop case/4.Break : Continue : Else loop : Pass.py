#  break ไว้ใช้หยุด loop
#  continue เอาไว้ใช้ข้ามโค๊ดส่วนอื่นๆภายใน loop
#  pass เอาไว้ผ่านตัวทำงานของฟังก์ชันเลย

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for day in week:
    if day == "Wed":
        print("Best day = ", day)
        break
    else:
        print("Not the day Keep finding")

n = int(input())
Sum = 0
for i in range(2, n + 1):
    if i % 2 != 0:
        continue
    else:
        print(i)
        Sum += i  # Sum ดิมบวกเพิ่ม i ใหม่
print("Sum = ", Sum)

for letter in "Python":
    if letter == 'h':
        pass
    else:
        print("Current is ", letter)

for num in range(0, 5):
    if num % 2 == 0:
        print(num, "can mod")
        break
else:
    print("end")

ki = 0
while ki > -1:
    ki += 1
    if ki == 3:
        ki = -10
else:
    print("Just end while")

print(sep='')
