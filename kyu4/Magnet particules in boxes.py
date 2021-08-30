'''
Professor Chambouliard hast just discovered a new type of magnet material.
He put particles of this material in a box made of small boxes arranged in K rows and
N columns as a kind of 2D matrix K x N where K and N are postive integers.
He thinks that his calculations show that the force exerted by the particle in the small box (k, n) is:


Task:
To help Professor Chambouliard can we calculate the function doubles
that will take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)?
Experiences seems to show that this could be something around 0.7 when maxk and maxn are big enough.
'''


def doubles(maxk, maxn):
    res = 0
    for k in range(1, maxk+1):
        resu = 0
        for n in range(1,maxn+1):
            resu += (n+1)**(-2*k)
        res += resu/k
    return res