'''
Created on 1 Sep 2021

@author: dankmint
'''

def thePrintFunction(n):
    z =''
    for x in range(1,n+1):
        z += str(x)
    print(z)
    

if __name__ == '__main__':
    n = int(input())
    thePrintFunction(n)