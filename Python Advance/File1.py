#prevent unwanted codes to second file


import os 


def main():
    print(os.listdir('/'))
    print('this is just a sentence which we will not call in File1a file')

if (__name__== '__main__'): #this code will prevent from calling unwanted in file1a
    main() 



def veryImport(): #only this will print
    return 'This is the line should come in File1a file'