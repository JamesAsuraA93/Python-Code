# ============================= #
#                               #
#    Welcome to Shopkeeper      #
#                               #
# All tools feels like product  #
#                               #
# ============================= #


class ShopKeeper:
    __TAX = 0.07  # ตั้งตัวแปร constance เพื่อบอกว่าไม่ควรเปลี่ยนค่า และเป็นตัวแปร private ใน class

    Welcome = "Welcome to our shop hope you'll be great to be here!"
    Preview = "My Shop have 1: Rose, 2: Lily, 3: Sunflower, 4: Carnation"
    None_of_Above = "You put it wrong please input again."

    def Cost_vat(self, money):
        return (self.__TAX * money) + money

    @staticmethod
    def Pick_Flower(match):
        switch = {
            1: "Rose",
            2: "Lily",
            3: "Sunflower",
            4: "Carnation"
        }
        return switch.get(match, "ERROR")

    @classmethod
    def Announce(cls, isAnnounce):
        if isAnnounce:
            return cls.Welcome + "\n" + cls.Preview
        else:
            return None


class Promotion(ShopKeeper):
    Pro_first = 0.90
    Pro_second = 0.95
    Pro_third = 0.98
    Pro_fourth = 1

    def Cost_Promotion(self, money, type_promo):
        if type_promo == 1:
            money *= self.Pro_first
        elif type_promo == 2:
            money *= self.Pro_second
        elif type_promo == 3:
            money *= self.Pro_third
        else:
            money *= self.Pro_fourth
        return money


def Cost(choice):
    tuple_cost = (20, 30, 40, 50)
    return tuple_cost[choice - 1]


Shop = ShopKeeper
Pro = Promotion
print(Shop.Announce(True))
while True:
    type_flower = int(input("You can put [1,2,3,4] : "))
    if Shop.Pick_Flower(type_flower) == "ERROR":
        print(Pro.None_of_Above)
        continue
    else:
        print(f"You pick a {Pro.Pick_Flower(type_flower)}")
        break

while True:
    prize = int(input("How much do you want to buy? : "))
    if prize <= 0:
        print(Pro.None_of_Above)
        print("Prize must be more than 0 !")
        continue
    else:
        money = Cost(type_flower) * prize
        print(f"All Cost {Shop.Cost_vat(ShopKeeper, money)}")
        type_coupon = int(input("What's tag coupon is yours [1,2,3] : "))
        money = Pro.Cost_Promotion(Promotion, money, type_coupon)
        print(f"Result cost you must pay = {Pro.Cost_vat(ShopKeeper, money)}")
        break

del money, prize, Shop, Pro, type_coupon, type_flower
