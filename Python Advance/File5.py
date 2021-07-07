#list, dict, gen comprehension 

numlist = [98,65,651,98,4,16,51,6,784,651,651,6,8,61,65,165,116,8,9,18,]
d4 = []
for item in numlist:
    if item % 4 ==0:
        d4.append(item)
print(d4)

#or
print('with list comprehension', [item for item in numlist if item%4==0]) 

#set
titan = {i ** 2 for i in [1,1,1,1,1,1,5,5,5,5,5,3,8,9,9,9,9,9,9,9]}
print(titan)

#dictionary
d1 = {'a':99, 'B':89, 'b':1}
print({r.lower():d1.get(r.lower(),0)+d1.get(r.upper(),0)for r in d1.keys()}) #it will do B + b

#generator

genesys = (i for i in range(56) if i%5==0)
for item in genesys:
    print(item)