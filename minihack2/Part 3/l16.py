# percent average
q = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
s = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
n = [150300, 247100, 333300, 266800, 420900, 318000]
percent = []
area = 0
for x in range( len(n) ) : 
    area = round(n[x] / s[x])
    percent.append(area)
for y in range( len(n) ) : 
    print("District", q[y], "has population rate:", percent[y])
ap = round( sum(percent) / len(q) )
print("The average population percentile is", ap)