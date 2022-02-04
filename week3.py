# ข้อ 1.จงหาผลลัพธ์ที่เป็นผลหารจากการหาร 59 ด้วย 6
print(59/6)

#2.จงหาผลลัพธ์ที่เป็นจำนวนเต็มจากการหาร 59 ด้วย 6
print(59//6)

#3.จงหาผลลัพธ์ที่เป็นเศษเหลือที่เป็นจำนวนเต็มจากการหาร 59 ด้วย 6
print(59%6)

#4.จงหาผลลัพธ์ที่เป็นผลหารจากการหาร -59 ด้วย 6
print(-59/6)

#5.จงหาผลลัพธ์ที่เป็นจำนวนเต็มจากการหาร -59 ด้วย 6
print(-59//6)

#6.จงหาผลลัพธ์ที่เป็นเศษเหลือที่เป็นทศนิยมจากการหาร -59 ด้วย 6
print(-59%6)

#7.จงตรวจสอบว่า 45 | 5 จริงหรือไม่ (ถ้าจริงแสดงข้อความ True ไม่จริงแสดงข้อความ False)
if 5%45 == 0:
    print('True')
else:
    print('False')
print(5%45)

#8. จงตรวจสอบว่า 5 | 45 จริงหรือไม่ (ถ้าจริงแสดงข้อความ True ไม่จริงแสดงข้อความ False)
if 45%5 == 0:
    print('True')
else:
    print('False')
print(45%5)

#9. จงรับค่าจำนวนเต็ม 3 ค่าจากผู้ใช้ผ่านหน้าจอ เก็บค่าไว้ในตัวแปร a, b, c จากนั้นทำการตรวจสอบว่า  ถ้า a|b และ a|c จริง ให้ทำแสดงค่าความจริงของการตรวจสอบ a|(b+c) กรณีอื่น แสดงค่าความจริงของการตรวจสอบ a|(b+c)
n = 787
if n > 1:
  for i in range(2, n):
    if (n % i) == 0:
      print(n, "is not a prime number")
      print('Because ',n,"=",i, "*", n // i)
      print('ตัวประกอบได้แก่ :')
      d = 2
      while  fac_> 1:
        if fac_ % d == 0:
          fac_ = fac_/d
          print(d)
        else:
          d = d+1
      break
  else:
    print(n, "is a prime number")
    
else:
  print(n, "is not a prime number")
  print('ตัวประกอบได้แก่ :')
  d = 2
  while  n> 1:
    if n % d == 0:
      n = n/d
      print(d)
    else:
      d = d+1

#11. จงตรวจสอบว่า 3851 เป็นจำนวนเฉพาะหรือไม่ ถ้าไม่เป็นจงบอกด้วยว่า มีเลขใดเป็นตัวประกอบ
n = 3851
if n > 1:
  for i in range(2, n):
    if (n % i) == 0:
      print(n, "is not a prime number")
      print('ตัวประกอบได้แก่ :')
      d = 2
      while  n> 1:
        if n % d == 0:
          n = n/d
          print(d)
        else:
          d = d+1
          break
  else:
    print(n, "is a prime number")
    
else:
  print(n, "is not a prime number")
  print('ตัวประกอบได้แก่ :')
  d = 2
  while  n> 1:
    if n % d == 0:
      n = n/d
      print(d)
    else:
      d = d+1

