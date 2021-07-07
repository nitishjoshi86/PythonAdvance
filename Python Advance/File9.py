""" import bisect

num = 4

a = [1,2,3,5,7,99]

print(bisect.bisect(a,num))
bisect.insort(a,num)
print(a) """

a = ['amit', 'binesh', 'vinod', 'rajan']
for i, item in enumerate(a):
    if (i+1)%2==0:
        print(item)