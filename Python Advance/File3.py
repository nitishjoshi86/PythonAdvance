#try, except, else, finally

""" try:
    open('file.txt')
except:
    print('File does not exist')


print('other code is fine') """

try:
    file = open('tutu.txt', 'r')
except Exception as e:
    print('File exists error')
else: #will print only if exception doesn't occur
     print('another exception ruled')
finally: #prints in every case
    print('it will print finally')
