# การตั้งชื่อ Dictionary >> Name_Variable = {Key:Info or Data}
Stupid_Person = {112: ["Prayut", 9, 'Male', 80000]}
# คีย์ของ Stupid_Person = 112  และมีชื่อ, อายุสมอง, เพศ, เซลล์สมอง


dic2 = {1: "John"}  # Key.dic2 = 1 Value.dic2 = "John"

dic3 = {"k1": 25.0, "k2": 12.0}  # Key ห้ามซ้ำกัน

dic4 = {35955: ["Ken", 22, 'M']}

dic5 = {35955: ["Elyne", 30, 'F']}

dic6 = {35955: ["Ken", 22, 'M'],
        35956: ["Jim", 21, 'M'],
        35957: ["Ja", 22, 'F'],
        35958: ["Ja", 22, 'F']}

print(dic3["k2"])  # 12.0
print(dic3["k1"], dic3["k2"], "\n")  # 25.0 12

print(dic4[35955], dic5[35955])
print(dic6[35955])
print(dic6[35957])

# dic3 = {"k1": 25.0, "k2": 12.0}  # Key ห้ามซ้ำกัน
print(dic3)
print(dic3["k2"])  # 12.0
dic3["k2"] = 20.9
print(dic3["k2"])  # 20.9
print(dic3, "\n")  # {'k1': 25.0, 'k2': 20.9}

# {'k1': 25.0, 'k2': 20.9}

print(dic3)  # {'k1': 25.0, 'k2': 20.9}
dic3["k3"] = dic3["k1"]
print(dic3)  # {'k1': 25.0, 'k2': 20.9, 'k3': 'abc'}

# .clear ลบแบบ Global ที่ Sync กัน
print(dic3.clear())  # None  สามารถ add ข้อมูลได้
print(dic3)  # {}

# การเพิ่ม Dictionary

add_dic = {}
add_dic['T'] = 123
print(add_dic)

dic7 = {"k2": 123, "J": 654}
dic_New = {}
dic_New["k2"] = dic7["k2"]
dic_New["J"] = dic7["J"]

del dic7["k2"]
print(dic7)
print(dic_New)

dic6 = {35955: ["Ken", 22, 'M'],
        35956: ["Jim", 21, 'M'],
        35957: ["Ja", 22, 'F'],
        35958: ["Ja", 22, 'F']}

print(len(dic6))  # 4

print(dic5.clear())  # None

print(dic6.get(35956))  # ['Jim', 21, 'M']
print(dic6[35956])  # ['Jim', 21, 'M']

print(dic6.items())
# dict_items([(35955, ['Ken', 22, 'M']), (35956, ['Jim', 21, 'M']), (35957, ['Ja', 22, 'F']), (35958, ['Ja', 22, 'F'])])

print(dic6.keys())  # dict_keys([35955, 35956, 35957, 35958])

print(dic6.values())  # dict_values([['Ken', 22, 'M'], ['Jim', 21, 'M'], ['Ja', 22, 'F'], ['Ja', 22, 'F']])
