'''
Created on 27 Oct 2021

@author: dankmint
For testing of word splitting
'''

if __name__ == '__main__':
    theword = 'insert 0'
    theword = theword.replace('insert', "")
    thelist = theword.split()
    print(thelist.pop())

    thewordlist = ['insert','remove']
    for x in thewordlist:
        print(x)
        if x in theword:
            print('okay')
            break