'''

Task
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane.
Its center (the intersection point of its diagonals) coincides with the point (0, 0),
but the sides of the rectangle are not parallel to the axes; instead,
they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside
the given rectangle (including on its sides)?

Example
For a = 6 and b = 4, the output should be 23

The following picture illustrates the example,
and the 23 points are marked green.


Input/Output
[input] integer a

A positive even integer.

Constraints: 2 ≤ a ≤ 10000.

[input] integer b

A positive even integer.

Constraints: 2 ≤ b ≤ 10000.

[output] an integer

The number of inner points with integer coordinates.
'''


#6,4 == 23
#30,2 == 65
import numpy as np
def rectangle_rotation(a, b):
    if 2 >= a >= 10000 and 2 >= b >= 10000: return None
    diag_a = a / np.sqrt(2) / 2
    diag_b = b / np.sqrt(2) / 2
    pro1 = [np.floor(diag_a) * 2 + 1, np.floor(diag_b) * 2 + 1]
    pro2 = []

    if diag_a - np.floor(diag_a) < .5:
        pro2.append(pro1[0] - 1)
    else:
        pro2.append(pro1[0] + 1)

    if diag_b - np.floor(diag_b) < .5:
        pro2.append(pro1[1] - 1)
    else:
        pro2.append(pro1[1] + 1)

    return pro1[0] * pro1[1] + pro2[0] * pro2[1]

print(rectangle_rotation(6, 4))
print(rectangle_rotation(30, 2))
