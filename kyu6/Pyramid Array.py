'''
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
Note: the subarrays should be filled with 1s
'''


def pyramid(n):
    res = []
    for i in range(n):
        r = []
        p = i
        while p >= 0:
            r.append(1)
            p -= 1
        res.append(r)
    return res

