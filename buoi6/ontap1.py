chuoi=(input("Mời nhập chuỗi: "))
print("Độ dài chuỗi: ", end="")
#Câu 1
print(len(chuoi))
#Câu 2

#Câu 3
cutfisrt=chuoi[:3]
cutlast=chuoi[-3:]
print(cutfisrt)
print(cutlast)
#Cau 4
print(chuoi.lower())
print(chuoi.upper())
#Câu 5
Ho=input("Mời nhập họ: ")
Tendem=input("Mời nhập tên đệm: ")
Ten=input("Mời nhập tên: ")
noichuoi=Ho + " " + Tendem + " " + Ten
print(noichuoi)