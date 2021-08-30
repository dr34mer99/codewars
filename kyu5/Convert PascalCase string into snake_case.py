'''
Complete the function/method so that it takes a PascalCase string and returns the string
in snake_case notation. Lowercase characters can be numbers.
If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
'''

def to_underscore(string):
    if type(string) == int:
        return str(string)
    if string[0].isnumeric():
        s = string[0]
    else:
        s = string[0].lower()
    for i in range(1,len(string)):
        if string[i].islower() or string[i].isnumeric():
            s += string[i]
        else:
            s+= '_'
            s+= string[i].lower()
    return s