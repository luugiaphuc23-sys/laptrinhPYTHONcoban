import math
a = float(input('Moi nhap a:'))
b = float(input('Moi nhap b:'))
c = float(input('Moi nhap c:'))
d= b*b-4*a*c

if (d < 0):
    print("PT vo nghiem")
elif d == 0:
    x = -b/2*a
    print(f"x co nghiem la {x}")
else:
    x1 = (-b+math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a
    print(f"PT co 2 nghiem x1={x1} va x2={x2}")