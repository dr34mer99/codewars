'''
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!
'''

def tower_builder(n):
    a=[]
    for x in range(1,n+1):
        a.append(('*'*(x*2-1)).center(n*2-1))
    return a