#iterables, iterators, iterations

def gen(n):
    for i in range(n):
        yield i

print(gen(999999999999999999999999))

for i in gen(99):
    print(i) 