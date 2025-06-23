# Two Sum:
# Given an array of integers and a target integer, return the indices of the two numbers that add up to the target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
#
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: (0, 1) (because nums[0] + nums[1] = 2 + 7 = 9)

from typing import List, Tuple, Optional

# Inneficient solution: works in 0(n^2) because of nested loop
# def two_sum(integers: List[int], target: int) -> Optional[Tuple[int, int]]:
#     for index1 in range(len(integers)):
#         for index2 in range(len(integers)):
#             if (not index1 == index2) and integers[index1] + integers[index2] == target:
#                 return (index1, index2)

#     return None

# Efficient solution, works in 0(n)
def two_sum(integers: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen = {}
    for index, number in enumerate(integers):
        complement = target - number

        if complement in seen:
            return (seen[complement], index)
        seen[number] = index

    return None



print(two_sum([2, 7, 11, 15], 9))     # Correct output: (0, 1)
print(two_sum([3, 2, 4], 6))          # Correct output: (1, 2)
print(two_sum([1, 5, 3, 7], 8))       # Correct output: (1, 2) or (0, 3)
print(two_sum([0, -1, 2, -3, 1], -2)) # Correct output: (3, 4)
print(two_sum([1, 2, 3], 7))          # Correct output: None
print(two_sum([3, 3], 6))             # Correct output: (0, 1)

