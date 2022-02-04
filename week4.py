#1. จงหา gcd(48, 384) = ?
a = int(input("Enter a : "))
b = int(input("Enter b : "))
x = a
y = b
while b>0:
  print('a = ', a, ' b = ', b, ' r = ', a%b)
  a, b = b, a % b
print('gcd(a,b) = ',a)

#2. จงหา lcm(26, 52) = ?
a = int(input("Enter a : "))
b = int(input("Enter b : "))
x = a
y = b
while b>0:
  print('a = ', a, ' b = ', b, ' r = ', a%b)
  a, b = b, a % b
print('lcm(a,b) = ',(x*y)//a)

#3. จงตรวจสอบว่า a  ≡  b (mod 8) หรือไม่ ถ้าคอนกรูเอนซ์แสดงข้อความ "True" ถ้าไม่คอนกรูเอนซ์แสดงข้อความ "False" โดยรับค่า a และ b จากผู้ใช้ผ่านหน้าจอ
print('Check that "a congruence b (mod m)"')
a = int(input("Enter a number of a: "))
b = int(input("Enter a number of b: "))
m = 8
if (m > 0):
  if ((a-b)% m) == 0:
    print("True")
  else:
    print("False")

#4. จงแสดงค่าของตัวแปร a ซึ่งมีค่าอยู่ในช่วงขอบล่าง-ขอบบนที่ผู้ใช้กำหนด โดยที่ a  ≡  b (mod c) โดยรับค่าขอบล่าง ค่าขอบบน ค่า b และ c จากผู้ใช้ผ่านหน้าจอ
lower = int(input("Enter a number of lower: "))
upper = int(input("Enter a number of upper: "))
b = int(input("Enter a number of b: "))
m = int(input("Enter a number of c: "))
print('Numbers of a that a congruence ',b,'( mod',m,')')
for a in range(lower,upper+1):
  if (m > 0):
    if ((a-b)% m) == 0:
      print(a,' congruence ',b,'( mod ',m,')')


#5. จงสร้างเลขสุ่มเทียม 8 จำนวน โดยใช้ : xn+1 = (2xn + c) mod 24 โดยรับค่า x0 และค่า c จากผู้ใช้ผ่านหน้าจอ
seed = int(input("Pls input number จำนวนเริ่มต้น  : "))
a = 2
c =  int(input("Pls input number ค่าเพิ่มขึ้น : "))
m = 24
n = 8
rn = seed
for i in range(1,n+1):
  rn = ((a * rn) + c) % m
  print(rn)

#6. จงรับค่า a และ b จากผู้ใช้ผ่านหน้าจอและตรวจสอบว่า a และ b เป็นจำนวนเฉพาะสัมพัทธ์หรือไม่
a = int(input("Plase input number of a : "))
b = int(input("Plase input number of b : "))
x = a
y = b
while b>0:
  a, b = b, a % b
gcd = a
if gcd == 1:
    print(x,'and',y,'are relatively prime')
else:
    print(x,'and',y,'are NOT relatively prime')


#7. จงตรวจสอบว่าชุดตัวเลข 13, 14, 51, 29, 11, 65 เป็นจำนวนเฉพาะสัมพัทธ์เป็นคู่หรือไม่
from math import gcd

def ischeckPairwise(A, n):
  for i in range(n):
    for j in range(n):
      if(i != j):
        if gcd(A[i],A[j]) != 1:
          print('gcd(',A[i],',',A[j],') =',gcd(A[i],A[j]))
          return False
  return True
A = [13, 14, 51, 29, 11, 65]
n = len(A)
if ischeckPairwise(A, n):
  print("pairwise relatively prime")
else:
  print("NOT pairwise relatively prime")

#8. จงเข้ารหัสข้อความ “happynewyear” แสดงผลลัพธ์ และถอดรหัสข้อความที่เข้ารหัสได้ เพื่อตรวจสอบว่าถูกต้องตรงกับข้อความต้นฉบับหรือไม่ 
#เมื่อกำหนดให้ฟังก์ชันที่ใช้ในการเข้ารหัส คือ f (a) = (a+s) mod m เมื่อ a คือตำแหน่งอักษรในข้อความต้นฉบับ s คือจำนวนตำแหน่งที่ต้องการเลื่อนไปจากตำแหน่งเดิม 
#m คือจำนวนตัวอักษรภาษาอังกฤษทั้งหมด
plaintext = "happynewyear"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = ""
s = int(input("Plase จำนวนที่ต้องการเลื่อน : "))
m = 26
new_ind = 0
for i in plaintext.upper():
    if i in alphabet:
      new_ind = alphabet.index(i) + s
      ciphertext += alphabet[new_ind % m]
    else:
      ciphertext += i
print("The ciphertext is: " + ciphertext)

#9. ทดลองใช้โปรแกรมในข้อ 8. เข้ารหัสข้อความ “merry x'mas 2021” แสดงผลลัพธ์ และถอดรหัสข้อความที่เข้ารหัสได้ เพื่อตรวจสอบว่าถูกต้องตรงกับข้อความต้นฉบับหรือไม่
plaintext = "merry x'mas 2021"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = ""
s = int(input("Plase จำนวนที่ต้องการเลื่อน "))
m = 26
new_ind = 0
for i in plaintext.upper():
    if i in alphabet:
      new_ind = alphabet.index(i) + s
      ciphertext += alphabet[new_ind % m]
    else:
      ciphertext += i
print("The ciphertext is: " + ciphertext)


#10. จงเข้ารหัสข้อความ “กลองของสมภพ” แสดงผลลัพธ์ และถอดรหัสข้อความที่เข้ารหัสได้ 
# เพื่อตรวจสอบว่าถูกต้องตรงกับข้อความต้นฉบับหรือไม่ (โดยเข้ารหัสเฉพาะพยัญชนะไทยเท่านั้น) เมื่อกำหนดให้ฟังก์ชันที่ใช้ในการเข้ารหัส คือ
plaintext = "กลองของสมภพ"
alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
ciphertext = ""
s = int(input("Plase จำนวนที่ต้องการเลื่อน "))
m = 44
new_ind = 0
for i in plaintext.upper():
    if i in alphabet:
      new_ind = alphabet.index(i) + s
      ciphertext += alphabet[new_ind % m]
    else:
      ciphertext += i
print("The ciphertext is: " + ciphertext)


#11. ทดลองใช้โปรแกรมในข้อ 9. เข้ารหัสข้อความ “กล้องของนางสาวสมร” แสดงผลลัพธ์ และถอดรหัสข้อความที่เข้ารหัสได้ เพื่อตรวจสอบว่าถูกต้องตรงกับข้อความต้นฉบับหรือไม่
plaintext = "กล้องของนางสาวสมร"
alphabet = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"
ciphertext = ""
s = int(input("Plase จำนวนที่ต้องการเลื่อน "))
m = 44
new_ind = 0
for i in plaintext.upper():
    if i in alphabet:
      new_ind = alphabet.index(i) + s
      ciphertext += alphabet[new_ind % m]
    else:
      ciphertext += i
print("The ciphertext is: " + ciphertext)