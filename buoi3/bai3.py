kq = True
while kq:
    try:
        n = int(input("Mời nhập số nguyên n: "))
        if n > 0:
            break
    except ValueError:
        print("Lỗi nhập dữ liệu!")

i = 1
while i <= n:
    print(f"{i}",end=" ")
    i += 1