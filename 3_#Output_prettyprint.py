import pprint

i = 0

data = [(i, {'แมว', 'กิน', 'ปลาทู', 'หนู', 'ขโมย', 'แอบ', 'กิน', 'ปลาทูของแมว'}) for i in range(3)]   # 0 > 1 > 2   range(b) > b-1
james = [(j, {'James'}) for j in range(1, 4)]  # 1 > 2 > 3

print(data, "\n")

pprint.pprint(data)

print(james)   # [(1, {'James'}), (2, {'James'}), (3, {'James'})]
print(type(james))
