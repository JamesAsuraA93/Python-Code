"""
# สร้าง Method

# Instance Method  ต้องมี Instance เรียกใช้งาน Class

class ClassName:
    def MethodName(self,parameter):

        return parameter

# Class Method  ไม่ต้องมี Instance สามารถใช้งาน Class ได้เลย

class ClassName:
    @classmethod

    def ClassMethodName(cls,parameter):

        return parameter with expression

# Static Method

class ClassName():
    @staticmethod
        def StaticMethodName(single parameter):

            return parameter with expression

"""


# Method

# Instance Method

class Cal_area1:
    def cal_rectangle(self, w, h):  # สร้าง method
        return w * h


# Class Method

class Cal_area2:
    @classmethod
    def cal_triangle(cls, b, h):
        return 0.5 * b * h


# Static Method

class Cal_area3:
    @staticmethod
    def cal_circle(r):
        return 3.14 * r ** 2


"""

สร้าง Instance ขึ้นมาเพื่อใช้งานต่อ 

object_name = ClassName():

instance_name => ชื่ออินสแนซืที่ต้องการสร้าง
class_name  => ชื่อคลาสที่ต้องการเข้าถึง

"""


# Example

class Cal_area4:
    def cal_square(self, x):
        return x ** 3

    def cal_cylinder(self, r, h):
        return 3.14 * (r ** 2) * h


cal = Cal_area4()

cal_sqr = cal.cal_square(4)

cal_cylind = cal.cal_cylinder(5, 6)

print(f"ลูกบาศก์ = {cal_sqr}")

print(f"ทรงกระบอก = {cal_cylind}")

"""

All method in one class

"""


class Calculate_Value:
    def cal_rectangle(self, w, h):
        return w * h

    @classmethod
    def cal_triangle(cls, b, h):
        return 0.5 * b * h

    @staticmethod
    def cal_circle(r):
        return 3.14 * r ** 2

    def cal_square(self, x):
        return x ** 3

    def cal_cylinder(self, r, h):
        return 3.14 * (r ** 2) * h


Calculate = Calculate_Value()  # สร้าง Instance

rectangle = Calculate.cal_rectangle(3, 4)

# rectangle2 = Calculate_Value.cal_rectangle(3, 4)  # ไม่สามารถทำได้

triangle = Calculate_Value.cal_triangle(5, 6)  # ดึงชื่อ class มาใช้ได้เลย

triangle2 = Calculate.cal_triangle(6, 7)  # ได้

circle = Calculate_Value.cal_circle(7)  # ดึงชื่อ class มาใช้ได้เลย

circle2 = Calculate.cal_circle(5)  # ได้

print(f"All Value is สี่เหลี่ยมผืนผ้า = {rectangle}, สามเหลื่ยม = {triangle}, วงกลม = {circle}.")
