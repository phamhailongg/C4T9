# combine của câu 18 đến câu 21
# 18
l = ['Spider Man', 'photography', 'music', 'Dragon Ball']
for i in range(3) : 
    l.append(input("Something you wanna add: "))
# 19 + 20
for n, hobby in enumerate(l) :
    print(n + 1, ". ", hobby.upper(), sep="")
print('')
# 21
for n, hobby in enumerate(l) :
    if "e" in hobby or "E" in hobby : 
        print(n + 1, ". ", hobby.upper(), sep="" )

