"""

Attribute
and
Constructor

"""


# Normal class แสดง Attribute ธรรมดา

class Paddle:
    color = 'red'  # Attribute
    wide = 20  # Attribute
    high = 50  # Attribute

    def showPaddle(self, name, isbn):
        self.isbnn = isbn
        self.names = name
        return self.names, Paddle.color, Paddle.wide, Paddle.high, self.isbnn


Pad_Src = Paddle()
Pad_Ivy = Paddle()

print(format(Pad_Src.showPaddle("MyPaddle", "Layvien")))
print(format(Pad_Ivy.showPaddle("IvyPaddle", "Linda")))

# Constructor
"""
# ผ่านค่าพารามิเตอร์

def __init__(self, parm1, parm2, parm3,...,parm_n):
    self.parm1 = parm1
    self.parm2 = parm2
    self.parm3 = parm3
    ...
    self.parm_n = parm_n
    
    
# ไม่ผ่านค่าพารามิเตอร์

def __init__(self):
    self.attribute1 = ""
    self.attribute2 = ""
    self.attribute3 = ""
    ...
    self.attribute_n = value
    
"""


class Game:
    def __init__(self, name, days, color, page, stdn):
        self.name = name
        self.day = days
        self.type = color
        self.page = page
        self.stdn = stdn

    def showGameDetail(self):
        return self.name, self.day, self.type

    def showGameRoot(self):
        return self.name, self.day, self.type, self.page, self.stdn


The_Game_Detail = Game("Piggi", 49, "Red", 15, "098813")
print(The_Game_Detail.showGameRoot())

The_Game_Detail.day = 66

print(The_Game_Detail.showGameDetail())

print(The_Game_Detail.showGameRoot())

Another_Game_Detail = Game("Miner", 13, "Blue", 8, "034231")
print(Another_Game_Detail.showGameRoot())

print(The_Game_Detail.showGameRoot())


class Robot():
    def __init__(self):
        self.name = ""
        self.type = ""
        self.code = ""

    def showRobotDetail(self):
        return self.name, self.type, self.code


The_Robot_B = Robot()
i = 0
m = []
while i < 3:
    x = input()
    m.append(x)
    i += 1

The_Robot_B.name = m[0]
The_Robot_B.type = m[1]
The_Robot_B.code = m[2]

The_Robot_A = Robot()
The_Robot_A.type = "A"
The_Robot_A.name = "AGE"
The_Robot_A.code = 2312

print(The_Robot_B.showRobotDetail())
print(The_Robot_A.showRobotDetail())
