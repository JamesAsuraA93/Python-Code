"""
# คลาสแม่
class Superclass:
    Statement(s)

# คลาสลูกที่สืบทอดจากคลาสแม่
class Subclass(Superclass):
    Statement(s)

"""


# คล้ายการสร้าง Instance ตัวแปรชื่อใหม่

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


class DetailGame(Game):
    pass


SuperInts = Game("Piggi", 49, "Red", 15, "098813")

SubInts = DetailGame("Miner", 13, "Blue", 8, "034231")

print(SuperInts.showGameRoot())

print(SubInts.showGameRoot())


class Mae_JOY:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def showJOY(self):
        return self.name, self.color


# เหมือนล่องหน

class Loong_JOY(Mae_JOY):
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def showJOY(self):
        return self.name, self.color
    """
    pass


Loong = Loong_JOY("James", "Blue")

print(Loong.showJOY())
