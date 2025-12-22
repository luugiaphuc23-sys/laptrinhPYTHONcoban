import random

so_luot = 1
diem = 0

print("Có 6 lượt quay, nếu số từ 1 đến 60 là thành công, 61 đến 100 là thất bại")
while so_luot <= 6:
    while True:
        try:
            quay = input(f"Nhập \"q\" để quay lần {so_luot}: ")
            if quay == "q":
                break
        except Exception:
            print(f"Nhập ko hợp lệ!")
    so_random = random.randint(1, 100)
    print(f"Quay lần {so_luot} được số: {so_random}")
    if so_random >= 1 and so_random <= 60:
        diem_cong = random.randint(5, 30)
        diem += diem_cong
        print(f"Thành công, cộng {diem_cong}")
        print(f"Điểm hiện tại: {diem}")
        if diem >= 80:
            break
    else:
        print(f"Thất bại, trừ 2 điểm")
        diem -= 2
        if diem < 0:
            diem = 0
        print(f"Điểm hiện tại: {diem}")
    so_luot += 1

if diem >= 80:
    print(f"Bạn đã chiến thắng với {diem} điểm")
else:
    print(f"Bạn đã thua với {diem} điểm")