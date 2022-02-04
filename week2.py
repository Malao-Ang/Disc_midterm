# กำหนดให้
# p แทนสตริง "Santa Claus is 1,750 years old as of 2021"
# q แทนสตริง "468963"
# t แทนสตริง "afternoon"
# r แทนลิสต์ [2,3,4,5]
# s แทนลิสต์ [2,3,4,5,6,6.7]

#ข้อ 1.จงหาค่าความจริงของ  ∀x(x≥6)  และ  ∃x(x≥6) เมื่อเอกภพสัมพัทธ์คือลิสต์ s
s = [2,3,4,5,6,6.7]
a = all(x >=6 for x in s)
b = any(x>= 6 for x in s)
print('1. ค่าความจริงของ  all(x>=6) คือ',a)
print('2. ค่าความจริงของ  any(x>=6) คือ',b)

#2. จงหาค่าความจริงของ  ∀x  (x เป็นจำนวนเต็ม) และ  ∃x  (x เป็นจำนวนเต็ม)เมื่อเอกภพสัมพัทธ์คือลิสต์ r
r = [2,3,4,5]
a = all(isinstance(x,int) for x in r)
b = any(isinstance(x,int) for x in r)
print('1. ค่าความจริงของ all  (x เป็นจำนวนเต็ม) คือ ',a)
print('2. ค่าความจริงของ  any  (x เป็นจำนวนเต็ม) คือ ',b)

#3. จงหาค่าความจริงของ  ∀x  (x เป็นจำนวนทศนิยม) และ  ∃x  (x เป็นจำนวนทศนิยม)เมื่อเอกภพสัมพัทธ์คือลิสต์ s
a = all(isinstance(x,float) for x in s)
b = any(isinstance(x,float) for x in s)
print('1. ค่าความจริงของ all  (x เป็นจำนวนทศนิยม) คือ ',a)
print('2. ค่าความจริงของ any  (x เป็นจำนวนทศนิยม) คือ ',b)

#4. จงหาค่าความจริงของ  ∀x  (x เป็นตัวเลข) และ  ∃x  (x เป็นตัวเลข) เมื่อเอกภพสัมพัทธ์คืออักขระในสตริง p
p = "Santa Claus is 1,750 years old as of 2021"
a = all(x.isdigit() for x in p)
b = any(x.isdigit() for x in p)
print('ค่าความจริงของall  (x เป็นตัวเลข) is',a)
print('ค่าความจริงของany (x เป็นตัวเลข) is',b)

#5. จงหาค่าความจริงของ  ∀x  (x เป็นตัวเลข) และ  ∃x  (x เป็นตัวเลข) เมื่อเอกภพสัมพัทธ์คืออักขระในสตริง q
q =  "468963"
a = all(x.isdigit() for x in q)
b = any(x.isdigit() for x in q)
print('ค่าความจริงของall  (x เป็นตัวเลข) is',a)
print('ค่าความจริงของany  (x เป็นตัวเลข) is',b)

#6. จงหาค่าความจริงของ  ∀x  (x เป็นตัวอักษร) และ  ∃x  (x เป็นตัวอักษร) เมื่อเอกภพสัมพัทธ์คืออักขระในสตริง q
a = all(x.isalpha() for x in q)
b = any(x.isalpha() for x in q)
print('ค่าความจริงของall (x เป็นตัวอักษร) is',a)
print('ค่าความจริงของany (x เป็นตัวอักษร) is',b)

#7. จงหาค่าความจริงของ  ∀x  (x เป็นตัวอักษร) และ  ∃x  (x เป็นตัวอักษร) เมื่อเอกภพสัมพัทธ์คืออักขระในสตริง t
t = "afternoon"
a = all(x.isalpha() for x in t)
b = any(x.isalpha() for x in t)
print('1. ค่าความจริงของall  (x เป็นตัวอักษร) is',a)
print('2. ค่าความจริงของany (x เป็นตัวอักษร) is',b)

#8. จงหาค่าความจริงของ  ∀x∃y(x/y=1)  เมื่อเอกภพสัมพัทธ์ของ x และ y คือลิสต์ r
ux = [2,3,4,5]
uy = [2,3,4,5]
print(list(list (x/y == 1 for y in uy) for x in ux))
print(all(any(x/y == 1 for y in uy)for x in ux))

#9. จงหาค่าความจริงของ  ∃x∀y(x/y=1)  เมื่อเอกภพสัมพัทธ์ของ x และ y คือลิสต์ r
print(list(list (x/y == 1 for y in uy) for x in ux))
print(any(all(x/y == 1 for y in uy)for x in ux))

#10. จงหาค่าความจริงของ  ∃x∃y(x/y=1)  เมื่อเอกภพสัมพัทธ์ของ x และ y คือลิสต์ r
print(list(list (x/y == 1 for y in uy) for x in ux))
print(any(any(x/y == 1 for y in uy)for x in ux))