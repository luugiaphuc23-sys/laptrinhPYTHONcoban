import math
sokm = int(input('Nhap so km:'))

if sokm < 1:
    print("Quảng đường đi không hợp lệ!")
elif sokm < 2:
    tien = 20000
elif sokm <= 5:
    tien = 20000 + (sokm - 1) * 16000
elif sokm <= 10:
    tien = 20000 + 4 * 16000 + (sokm - 5) * 13000
else :
    tien = 20000 + 4 * 16000 + 5 * 13000 + (sokm - 10)*10000
if tien > 200000:
    tien * 0.9

    print(f"Số tiền phải trả là {tien}")