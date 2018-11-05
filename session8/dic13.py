# Kết hợp in với lệnh if, hãy kiểm tra xem key ‘name', ‘nationality’ có nằm trong dictionary của em không và hiện ra thông báo tương ứng
d = {
    "Name" : "Phạm Hải Long",
    "Age" : 19,
    "Description" : "Chú ong chăm chỉ",
    "Hobby" : "Đọc sách"
}
k = input("Which key you choose to check? ")
if k not in ["Name", "Age", "Description", "Hobby"] : 
    print("Key", k, "does not exist in my dictionary")
else : 
    print("Key", k, "exists in my dictionary" )