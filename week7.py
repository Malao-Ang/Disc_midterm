#1. จงสร้างฟังก์ชัน f(x) =  ⌊ x/5 ⌋  โดยจะส่งผลลัพธ์กลับไป เมื่อ x คือจำนวนเต็มที่รับมาจากแป้นพิมพ์
import math
x = int(input("Pls input number in x"))
w = float(input("Pls input float in w"))
def f(x):
  return math.floor(x/5)

#1.1 จงสร้างฟังก์ชัน g(x) = 4x 2 -90 โดยจะส่งผลลัพธ์กลับไป เมื่อ x คือค่าที่รับมาจากแป้นพิมพ์
def g(x):
  return ((4*(x**2))-90)

#1.2 รับค่าจำนวนเต็ม x 1 ค่าจากผู้ใช้ผ่านหน้าจอ และรับค่า w เป็นจำนวนทศนิยมยาว 5 หลัก 1 ค่าจากผู้ใช้ผ่านหน้าจอ 
#และแสดงค่า x และค่าผลลัพธ์การปัดเศษเลขทศนิยมของเลข w ที่รับเข้ามา ให้เป็นเลขทศนิยม 2 หลัก ออกทางหน้าจอ
print(x)
print(round(w,2))

#1.3  แสดงค่าของ f(x) ออกทางหน้าจอ
print("f(x) = ",f(x))

#1.4แสดงค่าของ g(f(x)) และ f(g(x)) ออกทางหน้าจอ
print("g(f(x)) = ",g(f(x)))
print("f(g(x)) = ",f(g(x)))

#1.5หาค่าของ g 3 (x) แสดงผลออกทางหน้าจอ
print("g**3(x) = ",g(g(g(x))))


#2. จงสร้างฟังก์ชันสำหรับสร้างเซตที่มีชื่อว่า Input_data(n) : รับค่า argument n คือจำนวนสมาชิกที่ต้องการสร้างเซต A 
#โดยให้ผู้ใช้ป้อนจำนวนสมาชิกในเซต (n) ที่ต้องการสร้างผ่านหน้าจอ เช่น เมื่อผู้ใช้ป้อน 2 
#จะทำการเรียกฟังก์ชั่นในการสร้างเซต Input_data(2) และปรากฏข้อความให้ป้อนตัวเลข 2 ครั้ง เมื่อผู้ใช้ป้อนตัวเลขครบ 2 ครั้ง 
#ให้แสดงผลของเซตที่สร้างได้บนหน้าจอ เมื่อผู้ใช้ป้อน 4 จะทำการเรียกฟังก์ชั่นในการสร้างเซต Input_data(4) 
#และปรากฏข้อความให้ป้อนตัวเลข 4 ครั้ง เมื่อผู้ใช้ป้อนตัวเลขครบ 4 ครั้ง ให้แสดงผลของเซตที่สร้างได้บนหน้าจอ

def Input_data(n):
  X=set()
  for i in range (n):
    x = int(input("input number in set  :"))
    X.add(x)
  return X

#2.1 สร้างเซต A มีสมาชิกจำนวน 4 ตัว โดยเรียกใช้ฟังก์ชั่น Input_data(4)
A = Input_data(4)
print("A = ",A)
#2.2  สร้างเซต B มีสมาชิกจำนวน 3 ตัว โดยเรียกใช้ฟังก์ชั่น Input_data(3)
B = Input_data(3)
print("B = ",B)
#2.3  สร้างเซต C มีสมาชิกจำนวน 5 ตัว โดยเรียกใช้ฟังก์ชั่น Input_data(5)
C = Input_data(5)
print("C = ",C)
#2.4สร้างเซต D มีสมาชิกจำนวน 6 ตัว โดยเรียกใช้ฟังก์ชั่น Input_data(6) แสดงเซต A, B, C, D ที่ได้ออกทางหน้าจอ
D =  Input_data(6)
print("A = {}\nB = {} \nC = {}\nD = {}".format(A,B,C,D))

#2.5 สร้างฟังก์ชั่นสำหรับการสร้างแผนภาพเวนน์สำหรับ 2 เซต ชื่อ Plot_v2(set1,set2) โดยรับค่า argument 2 ค่า คือชื่อเซต 2 เซตที่ต้องการนำมาสร้างแผนภาพเวนน์
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
def Plot_v2(set1,set2):
  venn2(subsets=(set1,set2),set_labels = (set1,set2))
  plt.show()

#2.6 สร้างฟังก์ชั่นสำหรับการสร้างแผนภาพเวนน์สำหรับ 3 เซต ชื่อ Plot_v3(set1,set2,set3) โดยรับค่า argument 3 ค่า คือชื่อเซต 3 เซตที่ต้องการนำมาสร้างแผนภาพเวนน์
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
def Plot_v3(set1,set2,set3):
  venn3(subsets=(set1,set2,set3), set_labels = (set1, set2,set3))
  plt.show()

#2.7แสดงแผนภาพเวนน์ของเซต A และ C โดยเรียกใช้ฟังก์ชั่น Plot_v2(A,C) ที่สร้างไว้แล้ว
Plot_v2(A,C)
print()
#2.8 แสดงแผนภาพเวนน์ของเซต B และ D โดยเรียกใช้ฟังก์ชั่น Plot_v2(B,D) ที่สร้างไว้แล้ว
Plot_v2(B,D)
print()
# 2.9 แสดงแผนภาพเวนน์ของเซต A B และ C โดยเรียกใช้ฟังก์ชั่น Plot_v3(A,B,C) ที่สร้างไว้แล้ว
Plot_v3(A,B,C)
print()
# 2.10 แสดงแผนภาพเวนน์ของเซต B C และ D โดยเรียกใช้ฟังก์ชั่น Plot_v3(B,C,D) ที่สร้างไว้แล้ว
Plot_v3(B,C,D)

