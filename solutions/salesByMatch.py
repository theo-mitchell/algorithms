'''

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example

n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs

'''


def sockMerchant(n, ar):
    socksCount = {}
    numberOfPairs = 0
    
    for index, element in enumerate(ar):
        if element in socksCount:
            socksCount[element] += 1
        else:
            socksCount[element] = 1

    for value in socksCount.values():
        numberOfPairs += (value - (value % 2)) / 2
    
    return int(numberOfPairs)