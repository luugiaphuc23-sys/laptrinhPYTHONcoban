import HamUC_BC
while True:
    try:
        A = int(input("Mời nhập A: "))
        B = int(input("Mời nhập B: "))
        if A>0 and B>0:
            break
    except:
        print("Nhập sai kiểu dữ liệu!")

print(f"USCLN của {A} và {B} là {HamUC_BC.USCLN(A,B)}" )