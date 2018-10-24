for i in range(0, 21):
    print(i)
# print 0 - n, n = input from users
n = int(input())
for i in range(0, n + 1):
    print(i)
for i in range(5, 13):
    print(i)
# print 5 - n, n = input from users
n = int(input())
for i in range(5, n + 1):
    print(i)
for i in reversed(range(10, 21)):
    print(i)
# m -> n
n = int(input())
m = int(input())
o = int(input())
r4 = range(n, m, -o)
print(*r4)
