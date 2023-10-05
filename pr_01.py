#
# def division(num, div):
#     try:
#         rem = num/div
#         return rem
#     except Exception as e:
#         return e
#     finally:
#         return "Success"
# print(division(3,0))


# try:
#     raise NameError("It is an error")
# except NameError:
#     raise


# import requests
#
# #getting data from an api
# request = requests.get('https://reqres.in/api/users')
# print(request.json())
# data = {
#     "id" :"9",
#     "email" :"something@gmail.com",
#     # "first_name": "Something",
#     # "last_name": "Aurther",
#     # "avatar": "something.jpg"
# }
# #sending data to an API
# x = requests.post('https://reqres.in/api/users', data=data)
# print(x.json())





# def rotateArray(arr, k):
#     t = int(input())
#     for i in range(t):
#         left_arr = arr[0:k]
#         right_arr = arr[k:]
#         print(right_arr+left_arr)
# rotateArray([1,2,3,4,5], 2)

# def solve(A, B):
#     sm = 0
#     for i in range(A, B + 1):
#         if i % 7 == 0:
#             sm += i
#     return sm
#
# A = 14078
# B = 90461
# print(solve(A,B))

# def rotateLeft(d, arr):
#     # Write your code here
#     for i in range(d):
#         d = arr.pop(-1)
#         return [d] + arr
#
# s = '41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51'
# lst = list(map(int, s.split(" ")))
# print(lst)
# print(rotateLeft(10, lst))



# def factorial(n):
#     if n < 1:
#         return -1
#     else:
#         if n == 1:
#             return 1
#         else:
#             return n * factorial(n-1)
#
#
# print(factorial(3))