/*

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

*/ 

// Very janky initial solution.

function pivotIndexBad(nums: number[]): number {
    let pI = -1
    for (var i = 0; i < nums.length; i++) {
        let left = nums.slice(0, i);
        let right = nums.slice(i + 1);

        let leftSum = left.reduce(function (x, y) {
            return x + y;
        }, 0);

        let rightSum = right.reduce(function (x, y) {
            return x + y;
        }, 0);

        if (leftSum === rightSum) {
            pI = i;
            break
        }
            
    }

    return pI;
};

// Better way
function pivotIndex(nums: number[]): number {
    let pivotIndex = -1;
    const sum: number = nums.reduce((partialSum, a) => partialSum + a, 0);
    let leftSum: number = 0;

    for (var i = 0; i < nums.length; i++) {

        if (leftSum === sum - nums[i] - leftSum) {
            pivotIndex = i;
            console.log('assigned pi')
            break;
        }

        leftSum += nums[i];
    }

    return pivotIndex;
};