"""
Boolean operators ใช้เปรียบเทียบ statement ผลลัพธ์เป็น True หรือ False

and จะเป็น True ก็ต่อเมื่อ 2 กรณีเป็นจริงทั้งคู่นอกนั้นเป็น False

or จะเป็นจริง True ก็ต่อเมื่อ กรณีใดเป็นจริง จะเป็น False เมื่อทั้ง 2 กรณีเป็นเท็จ

not เอาไว้กลับค่าให้ตรงข้าม เช่น จาก True หากมี not ก็จะกลายเป็น False

ลำดับความสำคัญ ไม่ได้เริ่มจากซ้ายไปขวา แต่นับจาก not and และ or ตามลำดับ

if statement เอาไว้เช็คเงื่อนไขว่าเป็นจริงหรือไม่ ถ้าจริงก็จะทำงานในส่วนของ statement
(Python จะใช้ indentation ด้วย 4 spaces)


if condition:
    print("")

"""

name = "me"
if name == "me":
    pass
    # print("Hello me")

name1 = "A"

if name1 == "Chai":  # True
    print("Hello Chai")  # <<<
else:  # false
    print("Hello", name1)  # <<<

point = -1

if point >= 80:
    print("Grade A")
elif 80 > point >= 70:  # point < 80 and point >= 70
    print("Grade B")
elif 70 > point >= 60:
    print("Grade C")
elif point < 60 and point >= 50:
    print("Grade D")
elif point < 50 and point >= 0:
    print("Grade F")
else:
    print("Error")

"""
point = 82
if point >= 80:
    print("Grade A")
elif 70 <= point < 80:
    print("Grade B")
elif 60 <= point < 70:
    print("Grade C")
elif 50 <= point < 60:
    print("Grade D")
else:
    print("FFFFFFF")
"""

point = 62

if point >= 80:
    print("Grade A")
elif 70 <= point:
    print("Grade B")
elif 60 <= point:
    print("Grade C")
elif 50 <= point:
    print("Grade D")
else:
    print("FFFFFFF")

N = 12
F = 21
K = 18

if N > 10:  # 3
    if F <= 20:  # 2
        if K == 10:  # 1
            print("A")
        elif K < 10:
            print("B")
        else:
            if F == 15:  # 0
                print("C")
    else:
        print("D")
else:
    print("error")
