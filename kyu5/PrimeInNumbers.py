'''
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
'''

def prime_factors(n):
    czy = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czy.append(k)
        k += 1
    coun = {}
    i = 0
    while i < len(czy):
        if czy[i] not in coun.values():
            coun[str(czy[i])] = czy.count(czy[i])
        i+=1
    st = ''
    for i in coun:
        if coun[i] > 1:
            st += f'({i}**{str(coun[i])})'
        else:
            st += f'({i})'
    return st