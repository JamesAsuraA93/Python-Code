"""

6.สร้างชุดข้อมูลของตัวเองที่มีรูปแบบต่อไปนี้ด้วยลิสต์
    รหัสประจำตัวนักเรียน
    ชื่อเล่น
    อายุ
    เลขท้ายเบอร์โทร 4 หลัก

7.เพิ่มรหัสไปรษณีย์ไปยังลิสต์ในข้อ 6

8.ลบข้อมูลออกจากลิสต์ในข้อ 6 ให้เหลือเพียงชื่อเท่านั้น และแสดงออกมา

"""

James_list = [35955, "james", 19, 3145]
print(James_list)

James_list.append(54120)
print(James_list)

"""inx = James_list.index("james")
print(inx)"""

del James_list[0]  # ["james", 19, 3145]

del James_list[1:]  # ["james"]

print(James_list)