'''
Created on 27 Oct 2021

@author: dankmint
'''


"""insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list."""

def listingsystem(theCommandList):
    thelist =[]
    for thecommand in theCommandList:
        if 'insert' in thecommand:
            thecommand = thecommand.replace('insert', "")
            thecommandsplit = thecommand.split()
            thevalue = int(thecommandsplit.pop())
            theindex = int(thecommandsplit.pop())
            thelist.insert(theindex,thevalue)
        elif 'print' in thecommand:
            printfeature(thelist)
        elif 'remove' in thecommand:
            thecommand = thecommand.replace('remove', "")
            thecommandsplit = thecommand.split()
            thelist.remove(int(thecommandsplit.pop()))
        elif 'append' in thecommand:
            thecommand = thecommand.replace('append', "")
            thecommandsplit = thecommand.split()
            thelist.append(int(thecommandsplit.pop()))
        elif 'sort' in thecommand:
            sortfeature(thelist)
        elif 'pop' in thecommand:
            popfeature(thelist)
        elif 'reverse' in thecommand:
            reversefeature(thelist)


def printfeature(thearray):
    print(thearray)

def sortfeature(thearray):
    thearray.sort()
    return thearray

def popfeature(thearray):
    thearray.pop()
    return thearray

def reversefeature(thearray):
    thearray.reverse()
    return thearray

def theSplittingFunction(theString):
    print('splitting')


if __name__ == '__main__':
    N = int(input())
    theCommandList =[]
    theDefaultCommandList=['insert','print','remove','append','sort','pop','reverse']
    for x in range(N):
        '''print(x)'''
        '''To collect input from the user'''
        theCommandList.append(input())
        '''print(theCommandList)'''
    listingsystem(theCommandList)