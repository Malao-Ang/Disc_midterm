# กำหนดให้

# p แทนประพจน์ 3 มีค่ามากกว่าหรือเท่ากับ 1

# q แทนประพจน์ 8 มีค่าไม่เท่ากับ 18

# r แทนประพจน์ 20 มีค่าน้อยกว่าหรือเท่ากับ 20

# s แทนประพจน์ 25 มีค่าเท่ากับ 2 ยกกำลัง 5

# จงเขียนโปรแกรม เพื่อตอบคำถามข้อ 1. - 7. ต่อไปนี้

# จงหาค่าความจริงของประพจน์ p  ∨   ¬ q

# จงหาค่าความจริงของประพจน์  ¬ (s  ∧  r)

# จงหาค่าความจริงของประพจน์ (r ⊕ q)  →   ¬ s

# จงหาค่าความจริงของประพจน์ s ↔  ( ¬ r  ∧  q)

# จงหาค่าความจริงของประพจน์ (q ⊕  ¬ p)  ∨  (s → r)

# จงหาค่าความจริงของประพจน์  ¬ p  ∨  (p ⊕ q)

# จงหาค่าความจริงของประพจน์ (r → s)  ↔  ( ¬ r ∨ s)

# จงสร้างตารางค่าความจริงของประพจน์  ¬ p  →  (q ↔ r)

# จงสร้างตารางค่าความจริงเพื่อตรวจสอบว่า  ¬ ( ¬ s  ∨  r) สมมูลกับ (s  ∧   ¬ r) หรือไม่

# จงสร้างตารางค่าความจริงเพื่อตรวจสอบว่า p ⊕ ( ¬ q  ∨  s) เป็นสัจนิรันดร์หรือไม่
p = (3>=1)
q = (8!=18)
r = (20 <= 20)
s = (25 == (2**5))
# 1.จงหาค่าความจริงของประพจน์ p  or (not q)
print("1. p  or (not q) = ",p or (not q))

#2. จงหาค่าความจริงของประพจน์  ¬ (s  ∧  r)
print("2. not (s  and  r) = ",not(s and r))

#3.จงหาค่าความจริงของประพจน์ (r ⊕ q)  →   ¬ s
print("3. (r xor q) => not (s) = ",(r ^ q) or s)

#4. จงหาค่าความจริงของประพจน์ s ↔  ( ¬ r  ∧  q)
print("4. s ==  ( not r  and  q) = ",s == (not(r) and q))

#5. จงหาค่าความจริงของประพจน์ (q ⊕  ¬ p)  ∨  (s → r)
print("5. (q xor  not p)  or  (s => r) = ",(q ^ (not (p)))  or  (not(r) or s))

#6. จงหาค่าความจริงของประพจน์  ¬ p  ∨  (p ⊕ q)
print("6. not(p) or (p xor q) = ",not(p) or (p ^ q))

#7. จงหาค่าความจริงของประพจน์ (r → s)  ↔  ( ¬ r ∨ s)
print("7. (r => s)  ==  ( not (r) or s) = ",(not(r) or s)  ==  ( not (r) or s))

#8. จงสร้างตารางค่าความจริงของประพจน์  ¬ p  →  (q ↔ r)
import ttg
table_val = ttg.Truths(['p','q','r'],['not p','p == r','not(not p) or (q == r)'],ints = False)
print(table_val)

#9. จงสร้างตารางค่าความจริงเพื่อตรวจสอบว่า  ¬ ( ¬ s  ∨  r) สมมูลกับ (s  ∧   ¬ r) หรือไม่
table_val = ttg.Truths(['s','r'],['not((not s) or r)','s and not(r)','(not((not s) or r))==(s and not(r))'],ints = False)
print(table_val)

#10. จงสร้างตารางค่าความจริงเพื่อตรวจสอบว่า p ⊕ ( ¬ q  ∨  s) เป็นสัจนิรันดร์หรือไม่
table_val = ttg.Truths(['p','q','s'],['not q','not q or s','(not q) or s','p xor ((not q) or s)'],ints=False)
print(table_val)
