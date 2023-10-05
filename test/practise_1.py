

# str_1 = "the quick brown fox jumps on the lazy dog"
# wovels = 'aeiou'
# lst_wovels = []
# for i in str_1:
#     if i in wovels:
#         lst_wovels.append(i)
# lst = set(lst_wovels)
# print(list(lst))



# lst = [-1,-2,1,3,5,7,-5,-8,-3,-10, 8,9,10]
# pos_lst = []
# for i in lst:
#     if i>0:
#         pos_lst.append(i)
# print(lst)
# print(pos_lst)



# lst = [1,2,3,4,5,6,7,8,9]
# sq_lst = []
# for i in lst:
#     sq_lst.append(i**2)
# print(lst)
# print(sq_lst)


# lst = [i for i in range(21)]
# even_lst = []
# for i in lst:
#     if i%2 == 0:
#         even_lst.append(i)
# print(lst)
# print(even_lst)


# sentence = "the quick brown fox jumps over the lazy dog"
# lst = sentence.split()
# print(lst)


# sentence = "the quick brown fox jumps over the lazy dog"


# def setZeroes(A):
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             if A[i] < A[j]:
#                 A[i][j] = 0
#             elif A[i] == A[j]:
#                 A[i][j] = 0
#             print(A[i])
#
#
# A = [[1, 0, 1],
#      [1, 1, 1],
#      [1, 1, 1]]
#
# setZeroes(A)





# def staircase(n):
#     for i in range(n):
#         for j in range(n):
#             if i==j:
#                 print(" #", end="")
#         print()
#
# staircase(4)

# str1 = "Akash"
# print(str1[])


# s = input()
# ls = s.split('@')
# print(ls)
#
# if ls[1].endswith('.com'):
#     print('Valid email')


# def calclength(s):
#     count = 0
#     for i in s:
#         count+=1
#     return  count
# s = input("String : ")
# print(calclength(s))

# def frequency(s):
#     d = {}
#     for i in s.lower():
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
# n = input('String : ')
# print(frequency(n))



# def newString(s):
#     if len(s) < 2:
#         return "invalid string"
#     return s[:2]+s[-2:]
#
# s = input("String : ")
# print(newString(s))

# def changechar(s,symbol):
#     return s[0]+s[1:].replace(s[0], symbol)
# n = input('String : ')
# symbol = input('Symbol : ')
# print(changechar(n,symbol))

# def swapwords(s1, s2):
#     return s2[-2:]+s1[-1],s1[-2:]+s2[-1]
# s1 = input('String 1 : ')
# s2 = input('String 2 :')
# print(swapwords(s1,s2))


# def adding(s):
#     if s[-3:] == 'ing':
#         s = s+'ly'
#     else:
#         s = s+'ing'
#     return s
# s = input('String : ')
# print(adding(s))



# def longestwords(lst):
#     ls2 = []
#     for i in lst:
#         ls2.append(len(i))
#     return max(ls2)
#
# lst = ['akash', 'abc', 'tusk', 'ram']
# print(longestwords(lst))




# def removenthindex(s, idx):
#     return s[:idx]+s[idx+1:]
# s = input("String : ")
# idx = int(input("Index : "))
# print(removenthindex(s,idx))


# def swapfirstlast(s):
#     return s[-1]+s[1:-1]+s[0]
# s = input('string : ')
# print(swapfirstlast(s))

# def removeoddval(s):
#     n = s[::-2]
#     return n[::-1]
# s = input("String : ")
# print(removeoddval(s))


# def countwords(st):
#     lst = st.split()
#     count_dict = {}
#     for i in lst:
#         if i in count_dict:
#             count_dict[i] += 1
#         else:
#             count_dict[i] = 1
#     return count_dict
#
# str = 'i am the sam is i a good boy boy sam is not good he is bad'
# print(countwords(str))


# def changeCase(s):
#     print(s.upper())
#     print(s.lower())
#
# s = input("Input : ")
# changeCase(s)


# def selectlasttwo(word):
#     return word[-2:]*4
#
# s = input('Word : ')
# print(selectlasttwo(s))


# def firstthree(word):
#     return word[:3]
# s = input("Word : ")
# print(firstthree(s))


# def reversestring(word):
#     if len(word) % 4 == 0:
#         return word[::-1]
#     return -1
# s = input('Word : ')
# print(reversestring(s))



# def toupperstring(word):
#     count = 0
#     for i in word[:4]:
#         if i.isupper():
#             count += 1
#     if count>=2:
#         return word.upper()
#     return word
# s = input('String : ')
# print(toupperstring(s))




# str1 = "tvdsbj jsjdj\t"
# print(str1)
# print(len(str1))
# print(str1.rstrip())
# print(len(str1.rstrip()))


# def checkstartswith(word, c):
#     if word.startswith(c):
#         return word
#     else:
#         return False
# s = input('String : ').lower()
# c = input("Character : ").lower()
# print(checkstartswith(s, c))

# def getcurrentcharindex(word):
#     for i in range(len(word)):
#         print(f"Current character {word[i]} at index {i}")
#
# s = input("character : ")
# getcurrentcharindex(s)


# def lowecasefirst(word):
#     return word[0].lower()+word[1:]
#
# s = input('Word : ')
# print(lowecasefirst(s))

#
# def checkprime(n):
#     count = 0
#     if n == 1:
#         print('Not a Prime')
#     for i in range(1,n+1):
#         if n%i == 0:
#             count+=1
#     if count == 2:
#         print('Prime')
#     else:
#         print('Not a prime')
#
# n = int(input('Number : '))
# checkprime(n)




# def checkprime():
#     n = int(input("Number : "))
#     count_prime_num = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             count_prime_num+=1
#     if count_prime_num == 2:
#         print('Prime')
#     else:
#         print("Not Prime")
# checkprime


# def factoirial(n):
#     if n==1:
#         return n
#     return n * factoirial(n-1)
#
# print(factoirial(6))


# def factorial(n):
#     fact  = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factorial(5))


# import csv
# with open("TABLE_X_PART_CLASS_PARAMS.csv", mode='r') as file:
#     csv_reader = csv.reader(file)
#     for line in csv_reader:
#         print(line)


# def func(my_func):
#     def decorator():
#         print("Hello...")
#         my_func()
#     return decorator
#
#
# @func
# def my_func():
#     print('Test')
#
# my_func()

import time
import math

# def calculatetime(func):
#     def my_decorator(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print('Total time taken by ', func.__name__, end-begin)
#     return my_decorator
#
# @calculatetime
# def factorial(n):
#     time.sleep(2)
#     print(math.factorial(n))
# factorial(1000)



# def my_decorator(func):
#     def innerfunc(*args, **kwargs):
#         print("Hello "+ func(*args, **kwargs))
#     return innerfunc
#
# @my_decorator
# def greet():
#     return 'Saurabh'
# greet()






import tkinter as tk













# def my_decorator(test):
#     def inner_func(*args, **kwargs):
#         print(test.__name__)
#         test()
#     return inner_func



# @my_decorator
# def my_func():
#     print(10**2)
# my_func(10)

# @my_decorator
# def test1():
#     print('Hello')
#
# test1()

