# Tạo thêm 1 màu ở cuối list 
print("Our color list: ")
l = [ "blue", "red", "teal", "green" ]
print(*l, sep= ", ")
l.append(input("Enter a new color: "))
print(*l, sep= ", ")