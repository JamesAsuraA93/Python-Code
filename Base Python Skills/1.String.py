names = "test"
name = 'T'
hello = "Hello " + name
print(hello)  # Hello T

result = "abcdefg"  # 7

# a    b   c   d   e   f    g    null
# [0] [1] [2] [3] [4] [5] [6]   [7]# นับจาก หน้าไปหลัง    result[0]
# [-7] [-6] [-5] [-4] [-3] [-2] [-1] # นับจาก หลังไปหน้า

print(len(result))  # 7
print(result.index('c'), "\n")  # นับตัวแรก #
print(result[3])  # d
print(result[6])  # g
print(result[-2])  # f
print(result[-7])  # a

has_a = 'A' in "bcdAefg"
has_aefg = "Aefg" in "Aefgasd"  # สลับ หน้า in
has_k = 'k' in "bcdAefg"

print(has_a)  # True
print(has_aefg)  # True
print(has_k)  # False
print("\n")

phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
length = len(phrase)  # Function
# print(length)  # 88

string_A = chr(65)
print(string_A)
Ascii_B = ord('B')
print(Ascii_B, "\n")

Up = "JohnDoe".upper()  # JOHNDOE     # Methods
Down = "JohnDoe".lower()  # johndoe
RP_right = "JohnDoe".replace("Jo", "Ky")  # KyhnDoe
RP_wrong = "JohnDoe".replace("JD", "Ky")  # JohnDoe

print(Up)
print(Down)
print(RP_right)
print(RP_wrong)
