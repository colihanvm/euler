import math

num = 600851475143

p = 0

while num % 2 == 0:
    p = 2
    num = num/2
for i in range(3, int(math.sqrt(num)) + 1, 2):
    while num % i == 0:
        p = i
        num = num/i
if num > 2:
    p = num
    
print(p)
