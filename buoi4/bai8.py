while True:
    try:
        n = int(input(f'Mời nhập n: '))
        if n > 0:
            break    
    except ValueError:
        print("Lỗi kiểu dữ liêu!")

i=1
max = 0
min = 1000
while i<=n:
    try:
        so = int(input(f'Mời nhập số thứ {i}: '))
        i+=1
        if so>max:
            max=so
        if so<min:
            min=so
    except ValueError:
        print('Nhập số không hợp lệ!')
print(f"Số lớn nhất là {max}")
print(f"Số bé nhất là {min}")
