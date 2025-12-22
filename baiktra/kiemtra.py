import Ham
print("Nhập N:", end="")
N = Ham.nhapN()

print("Câu 11")
So = Ham.nhapN(N)
if Ham.soHH(So):
    print(f"Số {So } là số hoàn hảo!")
else:
    print(f"Số {So } không phải là số hoàn hảo!")
