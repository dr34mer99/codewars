

# s="466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
# def pos_average(s):
#     podzial=s.split(", ")
#     suma, caly = 0, 0
#     for i in range(len(podzial)-1):
#         for z in range(i+1, len(podzial)):
#             for x in range(len(podzial[i])):
#                 caly += 1
#                 if podzial[i][x] == podzial[z][x]:
#                     suma += 1
#     return suma / caly * 100, suma, caly, podzial[:-1], podzial[1:]

# def pos_average(s):
#     values = s.split(", ")
#     count, total = 0, 0
#     for i in range(len(values)-1):
#         for j in range(i+1,len(values)):
#             for k in range(len(values[i])):
#                 if values[i][k] == values[j][k]: count += 1
#                 total += 1
#     return count / total * 100

# print(pos_average(s))

#expected 26.6666666667



# def move_zeros(array):
#     for i in range(len(array)):
#         if array[i] == 0:
#             array.append(0)
#             array.pop(i)
#     return array
#
# # print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

#
# def christmas_tree(height):
#     s = ''
#     p=[u for u in range(1,height*2,2)]
#     for i,k in zip(range(height),p):
#         s += ('*'*k).center(height*2-1) + '\n'
#     return s[:-1]
# print(christmas_tree(6))


#f(16)=231

# def teol(n):
#     p, i = 0, 0
#     while i<n:
#         p+=p*(n-i)
#         i+=1
#     return p
#
# print(teol(5425))

#
# def range_of_u(range):
#     li = [1,1,2]
#     while len(li) <= range-1:
#         id1 = li[-1]
#         id2 = li[-2]
#         li.append(li[len(li)-id1]+li[len(li)-id2])
#     return li
#
# def length_sup_u_k(a, b):
#     if (type(a) or type(b)) != int:
#         return 0
#     elif (a or b) < 0:
#         return 0
#     lis , p = range_of_u(a), 1
#     for i in lis:
#         if i >= b:
#             p += 1
#     return p
#
# def comp(c):
#     if type(c) != int:
#         return 0
#     a, o = range_of_u(c), 0
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             o += 1
#     return o
#
#
#
# def u(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     res = [1, 1]
#     for i in range(2, n):
#         index1 = i - res[i-1]
#         index2 = i - res[i-2]
#         res.append(res[index1] + res[index2])
#     return res
#
# print(u(12))
# print(range_of_u(12))
# print(range_of_u(134)==u(134))
# print(length_sup_u_k(45,12))
# print(type('2'))
#
#
# def to_underscore(string):
#     if string[0].isnumeric():
#         s = string[0]
#     else:
#         s = string[0].lower()
#     for i in range(1,len(string)):
#         if string[i].islower() or string[i].isnumeric():
#             s += string[i]
#         else:
#             s+= '_'
#             s+= string[i].lower()
#     return s
#
# print(to_underscore('6Test7Controller'))
#
# import random
# import time
#
#
# # def zeros(n):
# #     if n == 0: return 0
# #     def silnia(z):
# #         h = 1
# #         for i in range(1,z+1):
# #             h *= i
# #         return h
# #     sil = silnia(n)
# #     stri = str(sil)
# #     a = 0
# #     for i in stri[::-1]:
# #         if i == '0':
# #             a += 1
# #         else:
# #             break
# #     return a
# # import random
#
# # def pin():
# #     i = [random.randint() for x in range(10)]
# #     j = [x for x in random.randrange(10)]
# #     k = [x for x in random.randrange(10)]
# #     l = [x for x in random.randrange(10)]
# #     suma = 0
# #     for s,y,z,a in zip(i,j,k,l):
# #         suma += s*y*z*a
# #     return i,j,k,l
# #
# # print(len([random.randint(x,10) for x in range(10)]))
#
# #
# # def domain_name(str):
# #     if 'www.' in str:
# #         s = str.split('.')
# #         for i in range(len(s)):
# #             if s[i] == 'www':
# #                 return s[i+1]
# #     else:
# #         s = str.split('//')[1]
# #         return s.split('.')[0]
# #
# #
# # print(domain_name('https://google-udsada.pl'))
#
#
# # def alphabet_war(f):
# #     f = ' ' + f + ' '
# #     l = {'w': 4, 'p': 3, 'b': 2, 's': 1, 't': 0}
# #     r = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'j': 0}
# #     left, right = 0, 0
# #     li = list(l)
# #     ri = list(r)
# #     for i in range(len(f)):
# #         if f[i] == 't':
# #                 try:
# #                     f[i - 1].replace(f[i - 1], ri[li.index(f[i - 1])])
# #                     f[i + 1].replace(f[i + 1], ri[li.index(f[i + 1])])
# #                 except:
# #                     f[i + 1].replace(f[i + 1], ri[li.index(f[i + 1])])
# #                 finally:
# #                     f[i - 1].replace(f[i - 1], ri[li.index(f[i - 1])])
# #
# #         elif f[i] == 'j':
# #             try:
# #                 f[i - 1].replace(f[i - 1], li[ri.index(f[i - 1])])
# #                 f[i + 1].replace(f[i + 1], li[ri.index(f[i + 1])])
# #             except:
# #                 f[i + 1].replace(f[i + 1], li[ri.index(f[i + 1])])
# #             finally:
# #                 f[i - 1].replace(f[i - 1], li[ri.index(f[i - 1])])
# #
# #     for i in f:
# #         if i in l.keys():
# #             left += l[i]
# #         elif i in r.keys():
# #             right += r[i]
# #
# #     if left > right:
# #         return 'Left side wins!'
# #     elif left < right:
# #         return 'Right side wins!'
# #     else:
# #         return "Let's fight again!"
#
# #
# # f ='sdjadaft'
# #
# # print(alphabet_war(f))
#
#
# # car = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# #
# # x = car.get("price")
# # print(x)
# #
# #
# #
# # def closest(s):
# #     strn = s.split()
# #     weight = [x for x in strn]
# #     w = []
# #     for i in weight:
# #         s = 0
# #         for j in i:
# #             s += int(j)
# #         w.append(s)
# #     p = {}
# #     for i in w:
# #         for j in w[1:]:
# #             if i != j:
# #                 p[str(i)+'-'+str(j)]=abs(i-j)
# #
# #     return w ,weight,min(p)
# #
# # print(closest(("103 123 4444 99 2000 ")))
#
#
# #binary
# # def decode_bits(bin_str):
# #     nums, tens = [int(x) for x in bin_str], 0
# #     for i,j in zip(range(len(nums)),range(len(nums),-1,-1)):
# #         tens += nums[i] * 2**(j-1)
# #         print(i,j)
# #     return int(tens)
# #
# # print(decode_bits('111'))
# #
# # def decode_bits(bin_str):
# #     nums, tens = [int(x) for x in bin_str], 0
# #     for i in range(len(nums)):
# #         if i % 2 != 0:
# #             tens += nums[i]
# #         else:
# #             tens -= nums[i]
# #     return tens
# #
# # print(decode_bits('11101010101110101010101'))
#
# #hexagon
# def hexa(num):
#     if  0 > num: num = 0
#     elif num >= 255: num = 255
#
#     a = hex(num).split('x')[1]
#     if len(a) >1:
#         return a.upper()
#     else:
#         return ('0' + a).upper()
#
# def rgb(r,g,b):
#      return hexa(r)+hexa(g)+hexa(b)
#
# print(rgb(254,254,254), hexa(-20))
#
#
# import numpy as np
# def matrix_mult(a, b):
#     c,d = np.array(a), np.array(b)
#     e = np.dot(c,d)
#     f = []
#     # for i in
#     return e
# print(matrix_mult([ [1, 2],
#     [3, 2] ], [ [3, 2],
#     [1, 1] ])[1,1]== matrix_mult([ [1, 2],
#     [3, 2] ], [ [3, 2],
#     [1, 1] ])[1][1])

# def sum_pairs(ints, s):
#     try:
#         for i in range(1, len(ints)):
#             if ints[i-1] + ints[i] == s:
#                 return [i, j]
#     finally:
#         for i in ints:
#             for j in ints[1:]:
#                 if i + j == s:
#                     return [i, j]
#
#     return None
#
# print(sum_pairs([10, 5, 2, 3, 7, 5],10))




# def valid_ISBN10(isbn):
#     s=0
#     if len(isbn) < 9:
#         return False
#     elif isbn[:-1].isdigit():
#         for i in range(1, len(isbn)):
#             s += int(isbn[i - 1]) * i
#         if isbn[-1] == 'X':
#             s += 10 * 10
#         elif isbn[-1].isdigit():
#             s += int(isbn[-1])*10
#     elif True:
#         for i in isbn[:-1]:
#             if i.isalpha():
#                 return False
#     if s % 11 == 0:
#         return True
#     else:
#         return False
#
# print(valid_ISBN10('1234554321'))
# def dirReduc(arr):
#     w = arr.count('WEST')
#     e = arr.count('EAST')
#     n = arr.count('NORTH')
#     S = arr.count('SOUTH')
#
#
#     nums = []
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1):
#             if (arr[i].upper() == 'NORTH' and arr[j].upper() == 'SOUTH') or
#             (arr[i].upper() == 'SOUTH' and arr[j].upper() == 'NORTH') or
#             (arr[i].upper() == 'WEST' and arr[j].upper() == 'EAST') or
#             (arr[i].upper() == 'EAST' and arr[j].upper() == 'WEST'):
#                 nums.append(i)
#                 nums.append(j)
#     for i in reversed(list(set(nums))):
#         arr.pop(i)
#     return list(set(arr))
# print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

# def isprime(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
#     p = int(n ** 0.5) + 1
#     for d in range(3, p, 2):
#         if n % d == 0:
#             return False
#     return True
# #for small numbers
# def gap(g, m, n):
#     o = []
#     for i in range(m, n + 1):
#         if isprime(i):
#             o.append(i)
#     for i in range(len(o) - 1):
#         if abs(o[i] - o[i + 1]) == g:
#             return [o[i], o[i + 1]]
#     return None
#
# # def gap(g, m, n):
#
#
# print(gap(2,100,110))
#
#
#
# class Robot:
#     def __init__(self, robot_1, robot_2, tactics):
#         self.robot_1 = robot_1
#         self.robot_2 = robot_2
#         self.tactics = tactics
#
#     def isfirst(self,robot_1, robot_2):
#         if robot_1['speed'] >= robot_2['speed']:
#             return robot_1
#         elif robot_1['speed'] < robot_2['speed']:
#             return robot_2
#         else:
#             return robot_1
#
#     def fight(self, robot_1, robot_2, tactics):
#         return True

# print(type(str([1,2,3])))
# Print iterations progress
# def printProgressBar (iteration, total, prefix = "", suffix = "", decimals = 1, length = 100, fill = "█"):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#     iteration   - Required  : current iteration (Int)
#     total       - Required  : total iterations (Int)
#     prefix      - Optional  : prefix string (Str)
#     suffix      - Optional  : suffix string (Str)
#     decimals    - Optional  : positive number of decimals in percent complete (Int)
#     length      - Optional  : character length of bar (Int)
#     fill        - Optional  : bar fill character (Str)
#     """
#     percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#     filledLength = int(length * iteration // total)
#     bar = fill * filledLength + "-" * (length - filledLength)
#     print("r%s |%s| %s%% %s" % (prefix, bar, percent, suffix), end = "r")
#     # Print New Line on Complete
#     if iteration == total:
#         print()
#
# #
# # Sample Usage
# #
#
# from time import sleep
#
# # A List of Items
# items = list(range(0, 57))
# l = len(items)
#
# # Initial call to print 0% progress
#
# for i, item in enumerate(items):
#     # Do stuff...
#     sleep(0.1)
# # Update Progress Bar
# printProgressBar(i + 1, l, prefix = "Progress:", suffix = "Complete", length = 50)

# def solution(number):
#
#     if number <= 0: return 0
#     sum = 0
#     for i in range(number):
#         if i % 3==0 or i % 5 == 0:
#             sum += i
#     return sum
#
# print(solution(16)==60)
# print(solution(10)==23)
# print(solution(20)==78)
# print(solution(15)==45)
# print(solution(6)==8)

# import random
# def permutations(string):
#     if len(string) == 1: return [string]
#     l = []
#     while len(l) <= len(string) + 2:
#         o = ''
#         s = list(string)
#         for i in range(len(string)):
#             u = random.choice(s)
#             o += u
#             s.remove(u)
#         if o in l:
#             continue
#         else:
#             l.append(o)
#     return l
# import time
# print(time.time())
# print(permutations('abba'))
# print(time.time())


# def find_it(seq):
#     p = set(seq)
#     o = {str(i): seq.count(i) for i in p}
#     for i in o.items():
#         if i[1] % 2 != 0:
#             return i[0]
#     return None

# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

# import numpy as np
# import matplotlib.pyplot as plt
# data = [[30, 25, 50, 20],
# [40, 23, 51, 17],
# [35, 22, 45, 19]]
# X = np.arange(4)
# fig = plt.figure()
# ax = fig.add_axes([0,0,2,1])
# ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
# ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
# ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
# plt.show()

# print(list(range(0.0001,3.14,0.001)))


import matplotlib.pyplot as plt
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(-np.pi, np.pi, 0.1)
# circle = []
# for i in x:
#     o = x**2 + x**2
#     circle.append(o)
#
# plt.plot(x, circle)
# plt.show()

# def get_most_profit_from_stock_quotes(q):
#     o = [0, q[0]]
#     for i in range(len(q)-1):
#         if q[i + 1] - q[i] >= 0:
#             o.append(q[i+1])
#         else:
#             return sum(o)*q[i+1]
#     return sum(q[:-1])
#
# print(get_most_profit_from_stock_quotes([1, 2, 3, 4, 5, 6]), 15)

# def sol_equa(n):
#     if n < 0: return []
#     z = []
#     x = [i for i in range(n)]
#     y = [i for i in range(n)]
#     for i in x:
#         for j in y:
#             if (i - 2 * j) * (i + 2 * j) == n:
#                 z.append([i, j])
#             else:
#                 pass
#     return z
#
# print(sol_equa(90054), [[4, 1]])


# def getweight(n):
#     s = 0
#     for i in n:
#         s += int(i)
#     return s
#
# def order_weight(s):
#     s = s.split()
#     return ' '.join(sorted(s, key=getweight))

# print(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")

# class RomanNumerals:
#
#     def ret_num(self, s):
#         api = {'I': 1, 'IV': 4, 'V': 5, 'X': 10,
#                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         if type(s) == str:
#             try:
#                 return api[s.upper()]
#             except:
#                 return None
#         elif type(s) == int:
#             try:
#                 for i, j in api.items():
#                     if j == s:
#                         return i
#             except:
#                 return None
#
#     def unity(self, num):
#         num = str(num)
#         a = []
#         for i in range(len(num)):
#             a.append(str(int(num[i]) * 10 ** (len(num) - i - 1)))
#         return a
#
#     def from_roman(self, letters):
#         pass
#     def to_roman(self, digits):
#         pass
#
# ob = RomanNumerals()
# print(ob.unity(2143))
# from math import pi, log, floor
#
# def converter(n, decimals=0, base=pi):
#     """takes n in base 10 and returns it in any base (default is pi
#     with optional x decimals"""
#
#     k = floor(log(base, n))
#     result = []
#     cyfra = 0
#     while k - 1 > - decimals - 1:
#         if len(result) == k: result += "."
#         num = floor((n / base ** (k - 1)) % base)
#         n -= num * base ** (k - 1)
#         num = str(num)
#         result += num
#     try:
#         if int(num) < 36:
#             return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[int(num)]
#     except:
#         pass
#
#     return ''.join(result)
# # print(converter(13, 0, 8))
#
# import math
# def f(n,b,l,r=''):
#  for i in range(int(math.log(n,b)),-l-1,-1):r+="%i"%(n/b**i)+'.'*(0==i);n%=b**i
#  return r
#
# print(f(10,0,16))


# def doubles(maxk, maxn):
#     res = 0
#     for k in range(1, maxk+1):
#         resu = 0
#         for n in range(1,maxn+1):
#             resu += (n+1)**(-2*k)
#         res += resu/k
#     return res
#
# print(doubles(1, 10), 0.5580321939764581)
# print(doubles(10, 1000), 0.6921486500921933)
# print(doubles(10, 10000), 0.6930471674194457)
# print(doubles(20, 10000), 0.6930471955575918)

# def wyplaszcz(lista):
#     ret = []
#     for x in lista:
#         if type(x)==type([]):
#             for y in wyplaszcz(x):
#                 ret.append(y)
#         else:
#             ret.append(x)
#     return ret
#
# def has_exit(maze):
#     b = [maze[0] , maze[-1]]
#     b.append([j[0] for j in maze])
#     b.append([k[-1] for k in maze])
#     b[0] = list(b[0])
#     b[1] = list(b[1])
#     b = wyplaszcz(b)
#     if ' ' in b:
#         return True
#     else:
#         return False
#
# maze = ["########",
#         "# # ## #",
#         "# #k#  #",
#         "# # # ##",
#         "# # #  #",
#         "#     ##",
#         "########"]
# print(has_exit(maze))
# def CountNWD(list):
#     NWD = 1
#     for i in list:
#         NWD = NWD * i
#     return NWD
#
# def CountNWW(x, y, NWD):
#     NWW = (x * y) / NWD
#     NWW = int(NWW)
#     return NWW

# def convert_fracts(lst):
#     mianownik = [j[1] for j in lst]
#     for i in range(lst):
#
#     podstawa = max(mianownik)
#     ret = []
#     for i in lst:
#         skalar = podstawa / i[1]
#         ret.append([skalar * i[0], podstawa])
#     return ret
# from fractions import Fraction
# print(Fraction(1,2))
# print(convert_fracts([[1, 2], [1, 3], [1, 4]]))

# def heart(size):
#     for row in range(size):
#         for col in range(size+1):
#             if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#                 print("*", end=" ")
#             else:
#                 print(end=" ")
#         print()
#
# print(heart(6))
# import setuptools
# print(help(setuptools.setup))
# import time
# print(dir(time))
# def timer(func, *args):
#     start = time.clock()
#     for i in range(1000):
#         func(*args)
#     return time.clock()
#
# def total(reps, func, *pargs, **kwargs):
#     repslist = list(range(reps))
#
#     start = timer(func)
#     for i in repslist:
#         ret = func(*pargs, **kwargs)
#     elapsed = timer - start
#     return (elapsed, ret)
#
# def add(a : str, b : str, c : str) -> str:
#     return a+b+c
# b = add('pass', 'szok', 'dash')
# print('czas funkcji zdefiniowanej: ', total(1000, add, 'mysz', 'david', 'adam'))
#
# def add(a, b, c):
#     return a+b+c
#
# print('czas funkcji niezdefiniowanej: ', total(1000, add, 'mysz', 'david', 'adam'))

# def myreversed(s : str) -> str:
#     s1 = ''
#     for i in range(len(s)):
#         s1 += s[len(s)-1-i]
#     return s1
#
# print(myreversed('abcdefghijk'))

# def my_enumerate(l):
#     for i in range(len(l)):
#         yield i, l[i]
#
# for i in my_enumerate([12,231,43,'fas,']):
#     print(i)

#
# for i in enumerate([12,231,43,'fas,']):
#     print(i)
