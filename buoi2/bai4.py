import math
try :
    nam = int(input("Mời nhập năm: "))
except :
    print("Không hợp lệ ")
else :
    duCan = nam % 10
    duChi = nam % 12
    namAL = ''
    can = ''
    chi = ''

    match duCan :
        case 0 : 
            can = "Canh"
        case 1 :
            can = "Tân"
        case 2 :
            can = "Nhâm"
        case 3 :
            can = "Quý" 
        case 4 :
            can = "Giáp"
        case 5 :
            can = "Ất"
        case 6 :
            can = "Bính"
        case 7 :
            can = "Đinh"
        case 8 :
            can = "Mậu"
        case 9 :
            can = "Kỳ"

    match duChi :
        case 0 : 
            chi = "Thâm"
        case 1 :
            chi = "Dậu"
        case 2 :
            chi = "Tuât"
        case 3 :
            chi = "Hợi" 
        case 4 :
            chi = "Ti"
        case 5 :
            chi = "Sửu"
        case 6 :
            chi = "Dần"
        case 7 :
            chi = "Mẹo"
        case 8 :
            chi = "Thìn"
        case 9 :
            chi = "Tỵ"
        case 10 :
            chi = "Ngọ"
        case 11 :
            chi = "Mùi"

    print(can,chi)
     