################################################

#    ชนิดข้อมูลของไพทอน ไพทอนมีชนิดข้อมูลพืนฐานอยู่ 5 ชนิดดังนี้
#    Numbers เก็บข้อมูลตัวเลข
#    String เก็บข้อมูลตัวอักษร
#    List เก็บข้อมูลได้มากว่า 1 ค่าใน 1 ตัวแปร หรือที่เรียกว่า compound type
#    Tuple อ่านว่า "ทูเพิล" เก็บข้อมูลได้มากว่า 1 ค่าใน 1 ตัวแปร ใช้สำหรับเก็บลำดับ หรือที่เรียกว่า sequence type
#    Dictionary เก็บข้อมูลได้มากว่า 1 ค่าใน 1 ตัวแปรเช่นกัน หรือที่เรียกว่า table type เทียบได้กับตัวแปร array ใน php

#    คำสงวน ในภาษาไพทอน   (หากต้องการใช้จริง ๆ สามารถใช้ตัวพิมพ์ใหญ่หรือ "_" >> class_data ได้)
#    and, as, assert, break, class, continue, def, del, elif, else, except,
#    exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass,
#    print, raise, return, try, while, with, yield

#################################################

#   Naming
#   การตั้งชื่อตัวแปรควรตั้งให้สอดคล้องกับความเป็นจริงหรือให้มีความหมาย


################
# Variables
# one to one
################

Score1 = 34
Age1 = 22
Career1 = "Doctor"
# or
Score2, Age2, Career2 = 34, 22, "Doctor"


################
# Variables
# many to one
################

Sum = Total = All = 0.0
print(All)
print(Total)
print(Sum)
# ทั้งหมดจะมีค่าเท่ากัน
