'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9 

The left-to-right diagonal = 1 + 5 + 9 = 15. The right-to-left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.
'''


def diagonalDifference(arr):
    diagonalOne = 0
    diagonalTwo = 0
    for index, row in enumerate(arr):
        diagonalOne += arr[index][index]
        diagonalTwo += arr[index][len(arr) - index - 1]
    
    print(diagonalOne)
    print(diagonalTwo)
    
    return abs(diagonalOne - diagonalTwo)