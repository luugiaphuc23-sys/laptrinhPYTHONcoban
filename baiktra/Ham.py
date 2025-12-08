def nhapN():
    while True:
        try:
            N = int(input())
            if N>0:
                break
        except ValueError:
            print("Lỗi nhập liệu!")
    return N

def soHH(N):
    tong = 0
    for i in range(1,N):
        if N%i==0:
            tong += i
    if tong == N:
        return True
    return False
