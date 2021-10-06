'''
Task
Implement a function which takes an array of nonnegative integers
and returns the number of subarrays with an odd number of odd numbers.
Note, a subarray is a contiguous subsequence.

Example
Consider an input:

[1, 2, 3, 4, 5]
The subarrays containing an odd number of odd numbers are the following:

[1, 2, 3, 4, 5], [2, 3, 4], [1, 2], [2, 3], [3, 4], [4, 5], [1], [3], [5]
The expected output is therefore 9.

Test suite
100 random tests, with small arrays, 5 <= size <= 200, testing
the correctness of the solution.

10 performance tests, with arrays of size 200 000.

The expected output for an empty array is 0, otherwise
the content of the arrays are always integers k such
that 0 <= k <= 10000.

Expected time complexity is O(n)
'''


def solve(arr):
    temp = [1, 0]
    val = 0
    for x in arr:
        val = (val + x) % 2
        temp[val] += 1
    return temp[0] * temp[1]
print(solve([2, 2, 5, 6, 9, 2, 11]))
