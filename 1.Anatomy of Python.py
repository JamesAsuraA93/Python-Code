# =================================== #   1
#
#   Comment
#   File name : Anatomy of Python for Preview Anatomy Python
#
#
import math as mt
# =================================== #


# =================================== #    2
def convert(temp, unit):
    unit = unit.lower()
    if unit == 'c':
        temp = 9.0 / 5.0 * temp + 32
        return temp
    if unit == 'f':
        temp = (temp - 32) / 9.0 * 5.0
        return temp

# =================================== #


# =================================== #    3

current_temp = int(input("อุณหภูมิปัจจุบัน : "))
unit = str(input("บอกยูนิตที่ต้องการ \'f\',\'c\' : "))
result = convert(current_temp, unit)

print(result)

print(mt.e)
# =================================== #
