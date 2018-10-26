# weather

import random
n = int(random.randint(0, 100))
print(n)

if n < 30 :
    print("Rainy")
elif n in range(30, 60) :
    print("Cloudy")
elif n > 60 :
    print("Sunny")

 