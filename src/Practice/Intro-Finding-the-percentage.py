'''
Created on 26 Oct 2021

@author: dankmint
'''

from decimal import Decimal

def findingpercentage(n,student_marks,query_name):
    '''print("n={} , student_marks={}".format(n,student_marks))'''
    theImptResult = student_marks.get(query_name)
    y = 0.0000
    for x in theImptResult:
        '''print('before{}'.format(y))'''
        y += x
        '''print('after{}'.format(y))'''
    overallResult = "{0:.2f}".format(y / len(theImptResult))
    '''print(theImptResult)
    print(y)'''
    print(overallResult)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    findingpercentage(n,student_marks,query_name)
