"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example:

There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5, 2/5 and 1/5.

Results are printed as:
0.400000
0.400000
0.200000
"""

def plusMinus(arr):
    positive = 0
    negative = 0 
    zero = 0 
    numberOfElements = len(arr) 
    
    for element in arr:
        if element > 0:
            positive += 1
        elif element < 0:
            negative += 1
        else:
            zero += 1
    
    print(round(positive/numberOfElements, 6))
    print(round(negative/numberOfElements, 6))
    print(round(zero/numberOfElements, 6))
