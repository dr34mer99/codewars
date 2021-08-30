'''
Create a function that returns a christmas tree of the correct height.

For example:

hieght = 5 should return:

    *
   ***
  *****
 *******
*********
Height passed is always an integer between 0 and 100.

Use \n for newlines between each line.

Pad with spaces so each line is the same length. The last line having only stars, no spaces.
'''


def christmas_tree(height):
    s = ''
    p=[u for u in range(1,height*2,2)]
    for i,k in zip(range(height),p):
        s += ('*'*k).center(height*2-1)
        if i==range(height)[-1]:
            continue
        else:
            s+='\n'
    return s