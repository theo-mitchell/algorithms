"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

"""

def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    currentIterationSum = 0
    
    for indexToIgnore in range(0, len(arr)):
        for index, value in enumerate(arr):
            if index == indexToIgnore:
                continue
            
            currentIterationSum += value
        
        if currentIterationSum > maxSum:
            maxSum = currentIterationSum
        if currentIterationSum < minSum or minSum == 0:
            minSum = currentIterationSum
        
        currentIterationSum = 0
        
    
    print(minSum, maxSum)