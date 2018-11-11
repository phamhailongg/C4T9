# check Quận
q = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
n = [150300, 247100, 333300, 266800, 420900, 318000]
minn = n[0]
minp = 0
for x in range(len(n)) : 
    if n[x] <= minn : 
        minn = n[x]
        minp = x 
print("District", q[minp], "has minimum citizens:", minn)
maxn = n[0]
maxp = 0
for x in range(len(n)) : 
    if n[x] >= maxn : 
        maxn = n[x]
        maxp = x 
print("District", q[maxp], "has maximum citizens:", maxn)