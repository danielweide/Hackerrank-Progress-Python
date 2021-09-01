'''
Created on 1 Sep 2021

@author: dankmint
'''


def weirdCheck(theNum):
    if theNum%2 == 0 and 2<=theNum<6:
        print('Not Weird')
    elif theNum%2 == 0 and 6<=theNum<21:
        print('Weird')
    elif theNum%2 != 0:
        print('Weird')
    elif theNum%2==0 and theNum>20:
        print('Not Weird')



if __name__ == '__main__':
    #n = int(input().strip())
    n = int(input())
    weirdCheck(n)
