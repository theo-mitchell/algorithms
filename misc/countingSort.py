'''
Note:
For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

Challenge:
Given a list of integers, count and return the number of times each value appears as an array of integers.

Function Description:
Complete the countingSort function in the editor below.

countingSort has the following parameter(s):
arr[n]: an array of integers

Returns:
int[100]: a frequency array

'''

def countingSort(arr):
    result = [0] * 100
    
    for element in arr:
        result[element] += 1
    
    return result