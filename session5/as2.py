# Viết một chương trình yêu cầu nhập vào một tháng trong năm, sau đó in ra tháng này là mùa nào của năm: Xuân, Hạ, Thu hay Đông

m = int(input("Month? "))

if m in range(1, 4): 
    print("Spring")
elif m in range(4, 7):
    print("Summer")
elif m in range(7, 10):
    print("Fall")
elif m in range(10, 13):
    print("Winter")
