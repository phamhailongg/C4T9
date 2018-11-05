# Lặp lại bài 5, với key và value nhập từ bàn phím
d = {
    "Name" : "Phạm Hải Long",
    "Age" : 19,
    "Description" : "Chú ong chăm chỉ",
    "Hobby" : "Đọc sách"
}
d[input("Key: ")] = input("Value: ")
print(d)