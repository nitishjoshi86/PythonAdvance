#args & kwargs, where * is args (argument) **(keyword argument)

def car(*args):
    print(type(args)) #type of args is Tuple
    if(len(args)==3):
        print('My car name is', args[0],', I bought it at ', args[1], 'from', args[2], 'showroom')
    else:
        print('My car name is', args[0],', I bought it at ', args[1])


another = ['Ford', 98000,]
"""car(*another) #it will convert list into Tuple

car('Tesla', 36000, 'Tesla Site not a ')
"""
def models(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print (key, value)

def major(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)


modeist = {"Tesla":3, 'Ford': 45, 'Maruti': 95, 'Hyundai':70}
models(**modeist)
major('general', *another, **modeist)