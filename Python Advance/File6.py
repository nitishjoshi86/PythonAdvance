#map, reduce, filter

""" def ren(n):
    return n**3   
l1 = [9,8,7,3]
sq = list(map(ren,l1))
print(sq) """

""" def great3(n):
    if n>3:
        return True
    else:
        return False
l2 = [9,9,8,7,-986,21,3,1,-53,-32,1]
great3 = list(filter(great3, l2))
print(great3) """

from functools import reduce

def sum(a, b):
    return a+b

l1 = reduce(sum, [99,98,98,98,9,8,9,898,98])
print(l1)

