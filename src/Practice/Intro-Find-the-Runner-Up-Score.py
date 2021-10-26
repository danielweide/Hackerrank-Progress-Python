'''
Created on 26 Oct 2021

@author: dankmint
'''


def runnerUpScore(n,arr):
    originallist = list(arr)
    '''print("x = {} ,z ={}".format(n,originallist))'''

    ''' Remove duplicates first'''
    modifiedlist = []
    [modifiedlist.append(x) for x in originallist if x not in modifiedlist]

    ''' Identify the max value'''
    max_value = max(modifiedlist)
    modifiedlist.remove(max_value)

    '''Identify the 2nd Max Value'''
    max_value = max(modifiedlist)
    print(max_value)





if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerUpScore(n,arr)