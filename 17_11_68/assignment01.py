

# [1] กำหนดความน่าจะเป็นเลือกกล่อง
pR = float(input("ใส่โอกาสเลือกกล่องแดง (เช่น 0.40): "))
pB = float(input("ใส่โอกาสเลือกกล่องน้ำเงิน (เช่น 0.60): "))

# [2] กำหนดจำนวนผลไม้ในกล่องแดง
apple_R = int(input("จำนวน Apple ในกล่องแดง: "))
orange_R = int(input("จำนวน Orange ในกล่องแดง: "))
total_R = apple_R + orange_R

# [2] กำหนดจำนวนผลไม้ในกล่องน้ำเงิน
apple_B = int(input("จำนวน Apple ในกล่องน้ำเงิน: "))
orange_B = int(input("จำนวน Orange ในกล่องน้ำเงิน: "))
total_B = apple_B + orange_B

# ความน่าจะเป็นหยิบผลไม้แต่ละชนิดจากแต่ละกล่อง
p_a_R = apple_R / total_R
p_o_R = orange_R / total_R

p_a_B = apple_B / total_B
p_o_B = orange_B / total_B

# ความน่าจะเป็นรวม
p_F_a = p_a_R*pR + p_a_B*pB
p_F_o = p_o_R*pR + p_o_B*pB

# Bayes: ความน่าจะเป็นว่ามาจากกล่องแดงเมื่อหยิบ Orange
p_R_given_O = (p_o_R * pR) / p_F_o

# -----------------------------
# แสดงผลลัพธ์
# -----------------------------
print("\n===== ผลลัพธ์ =====")
print("ความน่าจะเป็นหยิบได้ Apple : p(F=a) =", p_F_a)
print("ความน่าจะเป็นหยิบได้ Orange : p(F=o) =", p_F_o)
print("ความน่าจะเป็นมาจากกล่องแดงเมื่อหยิบ Orange : p(R|O) =", p_R_given_O)
