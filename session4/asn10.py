# In ra dãy số đếm ngược từ n đến m, với điều kiện n > m, n và m nhập từ bàn phím

n = int(input())
m = int(input())
o = int(input())
r4 = range(n , m - 1, -o)
print(*r4)