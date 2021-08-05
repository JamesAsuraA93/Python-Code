print()  # ช่องว่าง 1 บรรทัด

print("\n")  # ช่องว่าง 2 บรรทัด เริ่มจากบรรทัดแรก  หรือขึ้นบรรทัดใหม่

print("\n" * 5)  # ช่องว่าง 5 บรรทัด

print("\n")

print("\r")  # ขึ้นบรรทัดใหม่แบบไม่เพิ่มช่องว่าง   print()

print("\t")  # ขยับไป 1 indent หรือ 1 tab หรือ 4 space-bar

print("123", end='')  # Display 123 พร้อมจบบรรทัดด้วย ' ' << ช่องว่าง

print("123", "456", "789", sep="TTT")  # 123TTT456TTT789

print("*" * 5)  # *****   str * int
print(5 * 5)  # 25          int * int

price = 74
print("Price is ", price)  # Price is  74

Score, GPAX_Score = 85, 3.5

print("Score is", Score, "GPAX is", GPAX_Score)  # Score is 85 GPAX is 3.5

print(f"Score is {Score} GPAX is {GPAX_Score}")  # Score is 85 GPAX is 3.5

print(f'{Score}')

name = "Chai"
age = 15
fot = 3.5
print("Hello, My name is %s" % name)  # Hello, My name is Chai  %s > string
print("I'm %d years old" % age)  # I'm 15 years old   %d > integer
# print("I'm",age, "years old")  # Equal


print("This is 'T'.")  # This is 'T'.
# print("This is "T".")  # Wrong
print("This is \"T\".")  # This is "T".
print('I\'m james')

a = input()
print(a)

print("Enter your name")
name = input()
print("Name is", name)

name = input("Enter your name : ")
print("Name is", name)

Score = float(input("Your Score :"))
print(Score)

x = input("Enter multi inputs :").split(',')
print(x)
print(type(x))  # list
