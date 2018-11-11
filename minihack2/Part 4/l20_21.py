# add score
# present in order 
print("High scores:")
hs = [79, 85, 80, 89, 95, 69, 70, 99]
hs = sorted(hs, key = int, reverse = True)
for i in range(0, 5) :
    print(i + 1, ". " , hs[i], sep= '')

sc = int(input("Enter your new score: "))
print("High scores:")
hs.append(sc)
hs = sorted(hs, key = int, reverse = True)
for i in range(0, 5) : 
    print(i + 1, ". " , hs[i], sep= '')
