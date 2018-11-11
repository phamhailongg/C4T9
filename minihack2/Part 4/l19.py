# add score
# present in order 
print("High scores:")
hs = [79, 85, 80, 89, 95]
for i, n in enumerate(hs) : 
    print(i + 1, "." , n)

sc = int(input("Enter your new score: "))
print("High scores:")
hs.append(sc)
for i, n in enumerate(hs) : 
    print(i + 1, "." , n)
