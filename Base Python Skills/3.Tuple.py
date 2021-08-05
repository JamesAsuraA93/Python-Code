tup1 = ()
tup2 = (1, 1.5, "tup", 'T')
#       1    2    3     4   ตัวที่
#       0    1    2     3   ตำแหน่ง
#      -4    -3   -2   -1
print(tup2)

print(tup1[0])  # Out of range

#   ด้านหน้าจะลงตัว:ด้านหลังจะลบ 1
#   เหตุผลที่ต้องลบ 1 ด้านหลัง
# for i in range(0,5): # >> 0-4
# tup2 = (1, 1.5, "tup", 'T')
# 0 1 2 3  len() = 4   1 2 3 index(4) => ofr

print(tup2[2])  # "tup"
print(tup2[:2])  # ตั้งแต่แรกถึง 1         a:b   ! >b-1
print(tup2[2:])  # ตั้งแต่แรกถึง 2 ถึงสุดท้าย
print(tup2[1:3])  # ตั้งแต่ตำแหน่งที่ 1 ถึงตำแหน่งที่ 2
print(tup2[::])  # ทั้งหมด  print(tup2[::])   # ทั้งหมด
print(tup2[-2])  # ตำแหน่งลบ -2 => 2   = tup

# del tup2[1]  # doesn't support
del tup2

tup2 = (1, 1.5, "tup", 'T', 2, 3, 5, 6)

print(tup2[0:7:2])  # 0 ถึง 5 เว้นวรรค 2   # (1, 'tup', 2, 5)   a:b:c
