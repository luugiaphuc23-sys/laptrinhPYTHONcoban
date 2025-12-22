#Câu 1
dspt = [8.5,6.0,5.5,7.5,6.5,7.0,8.0,9.0]
tong = 0
for value in dspt:
    tong += value
dtb = tong/len(dspt)
print(f"Tong diem la: {tong}")
print(f"Diem trung binh la: {dtb}")

print("--Câu 2--")
while True:
    try:
        x=float(input("Nhập số lít nước:"))
        if x>=0:
            break
    except ValueError:
        print ("Nhập sai kiểu dư liệu")

tiennuoc=0
if x<=10:
    tiennuoc=x*7000
elif x<=20:
    tiennuoc=7000*10+(x-10)*9000
else :
    tiennuoc=7000*10+9000*10+(x-20)*12000
    

phi=tiennuoc*0.05
tongtien=int(tiennuoc+phi)
print (f"Tổng tiền nước: {tongtien}")

#Câu d
input_string = input("Nhập danh sách các số: ") #các số cách nhau bằng dấu cách
list = list(map(int, input_string.split())) # Chuyển chuỗi nhập vào thành một danh sách các số
print(f"List ban dau la: {list}")
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if(list[i] > list[j]):
            list[i],list[j]= list[j],list[i]
        continue
print(f"So sap xep tang dan la: {list}")
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if(list[i] < list[j]):
            list[i],list[j]= list[j],list[i]
        continue
print(f"So sap xep giam dan la: {list}")