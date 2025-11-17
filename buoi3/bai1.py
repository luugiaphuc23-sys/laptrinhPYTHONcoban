try:
    Van = float(input('Mời nhập điểm Van: '))
    Toan = float(input('Mời nhập điểm Toan: '))
    Anh = float(input('Mời nhập điểm Anh: '))
except ValueError:
    print("Nhập sai kiểu dữ liệu!")
else:
    diemtb = (Van + Toan + Anh)/3

    if Van < 0 or Van > 10 or Toan < 0 or Toan > 10 or Anh < 0 or Anh > 10 :
        print('Nhập không hợp lệ')
    else :
        if (diemtb >= 9):
            print('Học sinh Xuất Sắc')
        elif (diemtb >= 8):
            print('Học sinh Giỏi')
        elif (diemtb >= 6.5):
            print('Học sinh Khá')
        elif (diemtb >= 5):
            print('Học sinh Trung bình')
        else :
            print('Học sinh Yếu')
