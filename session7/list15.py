# Xoá phần từ có nội dung ‘LOL’ trong bài tập 14, nếu phần tử này không tồn tại, cần kiểm tra và báo lại
l = ['Spider Man', 'photography', 'music', 'Dragon Ball']
if 'LOL' in l : 
    l.remove('LOL')
    print(l)
else : 
    print("'LOL' element is not in list l")