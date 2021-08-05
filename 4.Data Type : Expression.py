Number1 = 1  # True
Number2 = 0  # False

neg = -2
pot = 3.5

print(bool(Number1))

print(bool(neg))  # True
print(bool(pot))  # True

one = 1
two = 2

print(one == two)  # False
print(bool(Number2))
print(Number2, "\n")

Integer = 30
Huge_INT = 30e12  # 30 x 10^12
Neg_INT = -15e6  # -15 x 10^6
Neg_degree = 15e-7  # 15 x 10^-7

FloatingPoint = 23.10  # 23.10
Huge_FLOAT = 23.20e8  # 2320000000.0 = 23.20 * 10^8
Neg_FLOAT = -19.30e8  # -19.30 x 10^8
Neg_degreeF = 15.45e-7  # 15.45 x 10^-7

Num_String = '123HH'
Num1_Str = "123"

Complex = 3 + 5j  # เจอได้ในมัธยมปีที่ 5 จำนวนเชิงซ้อน  3 + 5i
CPx1 = 2 + 4j
CPx2 = 1 + 2j

CPx_Sum = CPx1 + CPx2
CPx_Multi = CPx1 * CPx2

# print(CPx_Sum)   # (3+6j)
# print(CPx_Multi, "\n")  # (-6+8j)


# ====================== #
#       Convert          #
# ====================== #

float_number = float(10)  # แปลงค่า integer เป็น float 10.0

number = int(35.321)  # แปลงค่า float เป็น integer  35
number2 = int(39.9)  # 39
word = str(number)  # แปลงค่า integer เป็น string  "35"

print(number2)

# ====================== #
#        Extra           #
# ====================== #

Bin = 0b1100

Oct = 0o25

Hex = 0x18

print(Bin, Oct, Hex, "\n")

print(Bin)
print(bin(Bin))  # 0b1100
print(bin(12), "\n")

# 35(10) = 100011(2)

print(Oct)
print(oct(Oct))
print(oct(21), "\n")

print(Hex)
print(hex(Hex))
print(hex(24), "\n")
