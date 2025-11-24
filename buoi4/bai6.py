while True:
    try:
        n = int(input(f'Mời nhập n: '))
        if n > 0:
            break    
    except ValueError:
        print("Lỗi kiểu dữ liêu!")

for i in range(1,n):
    if i == 5:
        continue
    print(i)