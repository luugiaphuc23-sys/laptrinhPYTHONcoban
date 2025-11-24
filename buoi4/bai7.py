while True:
    try:
        n = int(input(f'Mời nhập n: '))
        if n > 1:
            break    
    except ValueError:
        print("Lỗi kiểu dữ liêu!")
for i in range(2,n):
    if i %1== 0 and i %i== 0:
        print(i)