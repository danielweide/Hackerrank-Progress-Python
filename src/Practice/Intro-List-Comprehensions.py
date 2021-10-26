'''
Created on 26 Oct 2021

@author: dankmint
'''


def theListComprehensions(x,y,z,n):
    '''z = ''
    for x in range(1, n + 1):
        z += str(x)'''
    print("x = {} , y ={} , z ={} , n={}".format(x,y,z,n))


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    theListComprehensions(x,y,z,n)