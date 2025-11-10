import math
a = int(input('Nhap a='))
b = int(input('Nhap b='))
c = int(input('Nhap c='))

if (a > 0 and b > 0 and c > 0 and a+b > c and b+c > a and a+c > b):
    print(f"3 canh co the tao thanh tam giac")
    cv = a + b + c
    p = 1/2*cv
    dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Chu vi tam giac la {cv} - Dien tich tam giac la {dt}")
else:
    print(f"3 canh khong tao thanh tam giac")