# แม่สูตรคูณ 
# แสดงแม่สูตรคูณ 2,3,4,5,6 
# 2*1 . . . . 2*2 
x = int(input("ป้อนแม่สูตรคูณเริ่มต้น : "))
y = int(input("ป้อนแม่สูตรคูณสิ้นสุด : "))
for i in range(x,y+1): 
    print("แม่ ",i)
    for j in range(1,13) : 
        print(i,'x',j ," = ",(i*j))
