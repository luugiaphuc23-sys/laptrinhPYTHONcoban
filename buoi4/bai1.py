while True:
    try:
        n = int(input('Mời nhập n: '))
        if n>0:
            break
    except ValueError:
        print("Lỗi kiểu dữ liêu!")
for i in range(n):
    if i %2== 0:
        print(i, end=" ")