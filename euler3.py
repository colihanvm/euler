num = 600851475143
primes = [i for i in range(2,num+1)]
p = 0

while p < len(primes):
    for i in range(primes[p]*2,num+1,primes[p]):
        if i in primes:
            primes.remove(i)
    p=p+1
    
print(primes)
