import math
try:
    thang = int(input("MỜI NHẬP THÁNG: "))
except:
    print("Lỗi cú pháp")
else:
    match thang:
        case 1|3|5|7|8|10|12:
            print("Tháng này có 31 ngày")
        case 4|6|9|11:
            print("Tháng này co 30 ngày")
        case 2:
            print("Tháng này có 28 hoặc 29 ngày")
        case _:
            print("Tháng không hợp lệ")
