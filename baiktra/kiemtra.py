import Ham
N = Ham.nhapN()
print("Nhập N:", end="")


print("Câu 11")
So = Ham.nhapN(N)
if Ham.soHH(So):
    print(f"Số {So } là số hoàn hảo!")
else:
    print(f"Số {So } không phải là số hoàn hảo!")
