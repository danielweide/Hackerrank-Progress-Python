'''
Created on 1 Sep 2021

@author: dankmint
'''

def theLoopFunctionCheck(n):
    #range starts from 0 to 20 
    for x in range(0,n):
        print(x*x)
        
        

if __name__ == '__main__':
    n = int(input())
    theLoopFunctionCheck(n)