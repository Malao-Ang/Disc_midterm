#1. จงเขียนโปรแกรมสร้างเซตของเลขจำนวนเต็ม A, B, C ตามเงื่อนไขและมีค่าอยู่ในช่วงเลข 1 ถึงเลขสิ้นสุดที่ผู้ใช้กำหนด โดยให้รับค่าสิ้นสุด(Upper) จากผู้ใช้ผ่านหน้าจอ จากนั้นทำการสร้าง
#เซต A มีสมาชิกเป็นจำนวนเต็มที่หารด้วย 4 แล้วเหลือเศษ 2 ที่มีค่าอยู่ภายในช่วงตัวเลข 1 ถึงค่าสิ้นสุดที่ผู้ใช้กำหนด
#เซต B มีสมาชิกเป็นจำนวนคู่ ที่มีค่าอยู่ภายในช่วงตัวเลข 1 ถึงค่าสิ้นสุดที่ผู้ใช้กำหนด
#เซต C มีสมาชิกเป็นจำนวนที่หารด้วย 4 ลงตัว ที่มีค่าอยู่ภายในช่วงตัวเลข 1 ถึงค่าสิ้นสุดที่ผู้ใช้กำหนด
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

stop = int(input(" plase input stop number set :"))
A = set()
for i in range(stop+1):
    if i%4==2:
        A.add(i)
print("set A = ",A)

print('=====')
B = set()
for i in range(1,stop+1):
    if i%2==0:
        B.add(i)
print("set B = ",B)

print('=====')
C = set()
for i in range(1,stop+1):
    if i%4==0:
        C.add(i)
print("set C = ",C)

print('=====')
#1.1 จงหาผลลัพธ์ของ B-(C ∪ A)
print("B - (C|A) = ",B - (C|A))

print('=====')
#1.2 จงหาผลลัพธ์ของ (C ∪ A) ⊕ (B ∩ A)
print((C|A) ^ (B & A))

print('=====')
#1.3 จงตรวจสอบว่า A ⊃ C หรือไม่ ถ้าเป็นแสดงข้อความ "A is a proper superset of C" ถ้าไม่เป็นแสดงข้อความ "A is not a proper superset of C"
if A > C:
    print("1.3 A is a proper superset of C")
else:
    print("1.3 A is not a proper superset of C")

print('=====')
#1.4 จงตรวจสอบว่า C ⊆ B หรือไม่ ถ้าเป็นแสดงข้อความ "C is a subset of B" ถ้าไม่เป็นแสดงข้อความ "C is not a subset of B"
if C <= B:
    print("1.4 C is a subset of B")
else:
    print("1.4 C is not a subset of B")

print('=====')
#1.5 จงตรวจสอบว่า A-B มีสมาชิกต่างกันทั้งหมดกับ C หรือไม่ ถ้าต่างกันทั้งหมดให้แสดงข้อความ "Disjoint" ถ้าไม่ต่างกันทั้งหมดให้แสดงข้อความ "Not disjoint"
if A - B == C:
    print("1.5 Disjoint")
else:
    print("1.5 Not disjoint")

#1.6 จงหาผลลัพธ์ของ B ∩ (C ∪ A) และ (B ∩ C) ∪ A และตรวจสอบว่า B ∩ (C ∪ A) เท่ากับ (B ∩ C) ∪ A หรือไม่ 
# ถ้าเท่าให้แสดงข้อความ "Equal" ถ้าไม่เท่าให้แสดงข้อความ "Not equal"
print("B ∩ (C ∪ A) = ",B & (C | A))
print("(B ∩ C) ∪ A = ",(B & C) | A)
print("(B ∩ (C ∪ A)) ∩ ((B ∩ C) ∪ A) = ",(B & (C | A))&((B & C) | A))
if (B & (C | A)) == ((B & C) | A):
    print("1.6 Equal")
else:
    print("1.6 Not equal")

print("====")
#1.7 เขียนโปรแกรมเพื่อสร้างแผนภาพเวนน์ของเซต A B และ C แสดงผลที่ได้ออกทางหน้าจอ
venn3(subsets=(A, B,C) , set_labels = ('A','B','C'))
plt.show()

#2. เขียนโปรแกรมสร้างเซต D ซึ่งเป็นเซตของจำนวนคู่ที่มีค่าอยู่ในช่วง 11 ถึง 25 และแสดงค่าของเซต D ที่ได้ออกทางหน้าจอ
D = set()
for i in range(11,25):
  if i % 2 ==0:
    D.add(i)

#2.1 กำหนดให้เซต E เป็นเซตว่าง จงเขียนโปรแกรมเพิ่มสมาชิกเข้าไปในเซต E อีก 4 จำนวน 
# โดยทำการรับค่าจำนวนเต็มจากผู้ใช้ผ่านหน้าจอโดยใช้คำสั่ง for เพื่อ รับค่าจากผู้ใช้ 4 รอบ และแสดงค่าของเซต E ที่ได้ออกทางหน้าจอ
E = set()
for i in range(4):
  e = int(input("Plase input number in set E :"))
  E.add(e)
print("2. set D = ",D)
print("2.1 set E = ",E)

#2.2 หาผลลัพธ์ของ E-D และแสดงผลที่ได้ออกทางหน้าจอ
print("2.2 E-D = ",E-D)

#2.3 จงหาเซตกำลังของ E-D จากนั้นนับจำนวนสมาชิกของเซตกำลังที่ได้ และแสดงผลลัพธ์ทั้งหมดที่ได้ออกทางหน้าจอ\
from more_itertools import powerset
powerseT =list(map(set, powerset(E-D)))
print("2.3 Powerset E-D = ",powerseT)

#2.4 หาผลลัพธ์ของ (E ⊕ D)  ∪  (E-D) และแสดงผลที่ได้ออกทางหน้าจอ
print("(E ⊕ D)  ∪  (E-D) = ",(E ^ D)  |  (E-D))

#3. จงเขียนโปรแกรมเพื่อสร้างแผนภาพเวนน์ ดังตัวอย่าง โดยให้นิสิตกำหนดสมาชิกภายใน เซต A เซต B และเซต C ด้วยตนเอง
#3.1 
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
A = set([5,10,15,20,25,30,35])
B = set(['Buu', 'CS', 'IT', 5,10,15])
C = set(['Buu'])
venn2(subsets=(A, B) , set_labels = ('A','B'))
plt.show()

#3.2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
A = set([5,10,15,20,25,30,35,40])
B = set([ 5,6,7])
C = set([5,10,15,21,22,23])
venn3(subsets=(A, B,C) , set_labels = ('A','B','C'))
plt.show()
