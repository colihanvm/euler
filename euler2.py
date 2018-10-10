end = 4000000
#end = 89
first = 1
second = 2
result = 0

def fib(f, s):
    if f >= end or s >= end:
        return (1-s%2) * s
    else:
        return (1-s%2) * s + fib(s, f + s)

print(fib(first, second))
