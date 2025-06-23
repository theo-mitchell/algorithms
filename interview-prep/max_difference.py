# Problem: Maximum Difference (Best Profit)
# Given an array of integers representing prices or values, find the maximum difference
# between two elements such that the larger element comes after the smaller element.
# Formally, find the maximum value of A[j] - A[i], where j > i.
#
# Example:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5 (Buy at 1 and sell at 6)
#
# Input: [7, 6, 4, 3, 1]
# Output: -1 (No profitable transaction possible)
#
# Constraints:
# - The array can contain negative numbers.
# - If no positive difference exists, return the maximum negative difference or -1 explicitly.

from typing import List


def max_difference(values: List[int]):
    max_diffrence_value = -1

    if len(values) < 2:
        return max_diffrence_value

    min_value = values[0]

    for value in values[1:]:
        current_diffrence_value = value - min_value
        if (current_diffrence_value > max_diffrence_value):
            max_diffrence_value = current_diffrence_value
        if (value < min_value):
            min_value = value

    return max_diffrence_value if max_diffrence_value > 0 else -1


print(max_difference([7, 1, 5, 3, 6, 4]))  # Correct output: 5 (buy at 1, sell at 6)
print(max_difference([7, 6, 4, 3, 1]))  # Correct output: -1 (no profitable difference)
print(
    max_difference([2, 3, 10, 6, 4, 8, 1])
)  # Correct output: 8 (buy at 2, sell at 10)
print(max_difference([10, 20, 30]))  # Correct output: 20 (buy at 10, sell at 30)
print(max_difference([30, 10, 8, 2]))  # Correct output: -1 (no profitable difference)
print(max_difference([1]))  # Correct output: -1 (array too short for difference)
print(max_difference([-1, -5, -3, -4]))  # Correct output: 2 (buy at -5, sell at -3)
