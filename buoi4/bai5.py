while True:
    try:
        n = int(input(f'Mời nhập bảng cửu Chương: '))
        break
    except ValueError:
        print("Lỗi kiểu dữ liêu!")
print(f"Bảng cửu Chương {n}")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")