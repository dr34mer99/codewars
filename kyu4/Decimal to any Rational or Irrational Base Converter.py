'''
I started this as a joke among friends, telling that converting numbers to other integer bases is for n00bs,
while an actual coder at least converts numbers to more complex bases like pi
(or π or however you wish to spell it in your language), so they dared me proving I was better.

And I did it in few hours, discovering that what I started as a joke actually has some math ground
and application (particularly the conversion to base pi, it seems).

That said, now I am daring you to do the same, that is to build a function so that it takes a number
(any number, you are warned!) and optionally the number of decimals (default: 0) and a base (default: pi),
returning the proper conversion as a string:

#Note In Java there is no easy way with optional parameters so all three parameters will be given;
the same in C# because, as of now, the used version is not known.

converter(13) #returns '103'
converter(13,3) #returns '103.010'
converter(-13,0,2) #returns '-1101'

I know most of the world uses a comma as a decimal mark, but as English language
and culture are de facto the Esperanto of us coders, we will stick to our common glorious traditions and uses,
adopting the trivial dot (".") as decimal separator; if the absolute value of the result is <1,
you have of course to put one (and only one) leading 0 before the decimal separator.

Finally, you may assume that decimals if provided will always be >= 0
and that no test base will be smaller than 2 (because, you know, converting to base 1 is pretty lame)
or greater than 36; as usual, for digits greater than 9 you can use uppercase alphabet letter,
so your base of numeration is going to be: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.

That is my first 3-languages-kata, so I count on you all to give me extensive feedback,
no matter how harsh it may sound, so to improve myself even further :)
'''


from math import pi, log

def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi
    with optional x decimals"""
    rep = []
    if n < 0:
        rep.append('-')
        n *= -1
    if n == 0:
        k = 0
    else:
        k = int(log(n, base))

    for i in [pow(base, p) for p in range(k, -1 - decimals, -1)]:
        rn = int(n / i)
        n -= rn * i
        rep.append('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[rn])
        if i == 1 and decimals > 0:
            rep.append('.')
    return ''.join(rep)