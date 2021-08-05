"""

1.จงสร้างสตริงข้อความดังต่อไปนี้ “Python Programming”

2.จากข้อความที่หนึ่งตัดเฉพาะข้อความ “Python” มาแสดงเท่านั้น

3.ให้รวมสตริง “Hello” และ “World” เข้าด้วยกัน (ต้องประกาศอย่างละหนึ่งตัวแปร)

4.ให้ลบคำว่า “Programming” ออกจากข้อแรก

5.ให้ลบตัวแปรที่เก็บสตริงของข้อแรกทิ้ง

"""

S1 = "Python Programming"

print(S1[:6])

hello = "Hello"

world = "World"

print(hello+world)

S1 = S1.replace("Programming",'')
print(S1)

del S1
