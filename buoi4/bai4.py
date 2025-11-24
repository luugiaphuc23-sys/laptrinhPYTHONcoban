i = 1
dem = 0
while(i<=10):
    try:
        so = int(input(f"Mời nhập so thu {i}: "))
        i += 1
        if so < 0:
            dem += 1
    except ValueError:
        print("Lỗi kiểu dữ liêu!")
print(f"Có {dem} số âm!")

