import hcn
try:
    cd = int(input("Mời nhập chiều dài: "))
    cr = int(input("Mời nhập chiều rộng: "))
except ValueError:
    print("Nhập sai kiểu dữ liệu!")
else:
    cvdt = hcn.tinhcvdt(cd,cr)
    print(f"cvhcn {hcn.tinhcvhcn(cd,cr)}")
    print(f"cthcn {hcn.tinhdthcn(cd,cr)}")
    print(f"cv {cvdt[0]} và dt {cvdt[1]}")
