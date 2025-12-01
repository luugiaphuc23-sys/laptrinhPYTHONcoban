def tinhcvhcn(cd,cr):
    cv = (cd + cr) * 2
    return cv

def tinhdthcn(cd,cr):
    dt = cd * cr
    return dt

def tinhcvdt(cd,cr):
    cv = (cd + cr) * 2
    dt = cd * cr
    return cv,dt 
try:
    cd = int(input("Mời nhập chiều dài: "))
    cr = int(input("Mời nhập chiều rộng: "))
except ValueError:
    print("Nhập sai kiểu dữ liệu!")
else:
    cvdt = tinhcvdt(cd,cr)
    print(f"cvhcn {tinhcvhcn(cd,cr)}")
    print(f"cthcn {tinhdthcn(cd,cr)}")
    print(f"cv {cvdt[0]} và dt {cvdt[1]}")
