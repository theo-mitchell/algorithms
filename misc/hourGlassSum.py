"""
Given 6x6 a 2D Array arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. 
The array will always be 6x6.

Example:

arr = 
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

The 16 hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

The highest hourglass sum is 28.
It is from the hourglass beginning at row 1, column 2:

0 4 3
  1
8 6 6

"""

def hourglassSum(arr):

    #Finding side_length is not neccecary for this specific problem since it is specified.
    #This is done just so the solution can work for any provided 'square'
    side_length = int(len(arr[0]) / 2 + 1)
    sums = []
    for i in range(0, side_length):
        top_row = arr[i]
        mid_row = arr[i+1]
        bot_row= arr[i+2]
         
        for x in range(0, side_length):
            hg_sum = 0
            hg_sum += sum(top_row[x:x+3])
            hg_sum += mid_row[x+1]
            hg_sum += sum(bot_row[x:x+3])
            sums.append(hg_sum)
        
    return max(sums)

arr = [[-9, -9, -9, 1, 1, 1], 
[0, -9, 0, 4, 3, 2],
[-9, -9, -9, 1, 2, 3],
[0, 0, 8, 6, 6, 0],
[0, 0, 0, -2, 0, 0],
[0, 0, 1,  2, 4, 0]]

print (hourglassSum(arr))