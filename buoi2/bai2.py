try:
    so = int(input("Mời nhập số: "))
except:
    print("Lỗi cú pháp")
else:
    if so %2== 0:
        print(f"{so}là số chẵn")
    else:
        print(f"{so}là số lẻ")