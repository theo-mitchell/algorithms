'''
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i < j and ar[i] + ar[j]  is divisible by l.

Example

ar = [1, 2, 3, 4, 5, 6]
k = 5

Three pairs meet the criteria: [1, 3], [2, 3] and [4, 6].


Function Description:

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array 
int ar[n]: an array of integers
int k: the integer divisor

Returns
- int: the number of pairs

'''

def divisibleSumPairs(n, k, ar):
    numberOfPairs = 0
    
    for index, value in enumerate(ar):
        for index1 in range(index + 1, len(ar)):
            if (value + ar[index1]) % k == 0:
                numberOfPairs += 1
    
    return numberOfPairs