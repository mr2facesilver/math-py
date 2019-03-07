import math
from typing import List
from decimal import *

line = '10  5 13  6 15 13  4  2 12 10 16 18 11 16  4  13  4 18 14 15'
def makelist(line):
    count=0
    for x in line:
        if x==' ':
            count = count+1
    print("number of item is " + str(count+1))
    line2 = line.replace(' ', ',')
    print('the unsorted list is:')
    print(line2)
    print(' ')
    sorted1 = line2.split(",", count) #turns the string into a list
    sortednum: List[int] = []
    alist: List[int] = []
    for x in sorted1:
        alist.append(int(x))
        sortednum.append(int(x)) #turns the string into a list
    sortednum.sort()
    print("The sorted list")
    print(sortednum)

    print("midrange =")
    midrange = (sortednum[-1] + sortednum[0])/2
    print(midrange)

    mean =62.232 #set mean(xbar) and SD
    SD =18.25
    print('the z score for each point')
    zScore: List[float] = []
    for x in alist:
        zScore.append(round(float((x-mean)/SD),3))  #3 decimal places
    print(zScore)

    percentile = (float(count/100)*float(83))
    print(Decimal(count/100))
    cei = math.ceil(percentile)
    print(" the percentile is ")
    print(sortednum[cei ])


line1 = '77 54 64 67 66 57 51 65 55 64 52 49 37 59 48 74 55 40 50 52 89 70 72 66 75 70 70 60 66 60 69 70 42 32 69 74 86 56 34 66 60 68 60 49 35 61 58 74 31 56'
makelist(line1)
print('*********************************************************')
line2 = '-10 1 -17 -3 -21 -15 0 -15 -11 -22 -26 -26 -14 -20 -1 -15 2 -23 -19 -25'
#makelist(line2)