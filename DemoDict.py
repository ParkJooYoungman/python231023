# DemoDict.py

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
print("park" in phone)
print("kang" not in phone)

p = phone
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone), id(p))

#장비관리
device = {"아이폰":5, "아이패드":10}
#입력
device["맥북"] = 10
#삭제
del device["아이폰"]
print(device)


for item in device.items():
    print(item)
for item in device.keys():
    print(item)
for item in device.values():
    print(item)

print(bool(0))
print(bool(device))
print(1<2)
print(1 != 2)
print(1==2)
print(True and True and True)
print(True and True and False)
print(True or False or False)
