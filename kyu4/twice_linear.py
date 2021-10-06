'''
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Example:
u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13,
then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...)
returns the element u(n) of the ordered sequence u (ordered
with < so there are no duplicates) .

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency
'''


def dblinear(n):
    u ,x, y = [1], 0, 0
    for i in range(n):
        x_n = 2 * u[x] + 1
        y_n = 3 * u[y] + 1
        if x_n < y_n:
            u.append(x_n)
            x += 1
        elif x_n == y_n:
            u.append(x_n)
            y += 1
            x += 1
        else:
            u.append(y_n)
            y += 1
    return u[n]

print(dblinear(30))