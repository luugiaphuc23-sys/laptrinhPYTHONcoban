import math
thang = int(input('Nhap thang:'))
match thang:
    case 1|2|3:
        print('Mua Xuan')
    case 4|5|6:
        print('Mua Ha')
    case 7|8|9:
        print('Mua Thu')
    case 10|11|12:
        print('Mua Dong')