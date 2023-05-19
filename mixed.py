# push zeroes to end, comma seperated, remove duplicates, printDict(), prime num, recursion

# # 68
# arr = [0,2,3,4,6,7,9,0]
# for i in arr:
#     if i == 0:
#         arr.remove(0)
#         arr.append(0)
# print(arr)

# # 69
# sen = input("Enter a comma sepreated sentence")
# lis = sen.split(",")
# lis.sort()
# sen = ",".join(lis)
# print(sen)

# # 70
# import math
# d = input("Enter a comma seperated sentence: ")
# list = d.split(",")
# ans = []
# for val in list:
#     valint = int(val)
#     f = math.sqrt((2*50*valint)/30)
#     ans.append(str(int(f)))
# print(','.join(ans))

# # 71
# ans = []
# list = [12,24,35,24,88,120,155,88,120,155]
# for i in list:
#     if not i in ans:
#         ans.append(i)
# print(ans)

# # 72
# n = int(input("Enter n"))
# def printDict():
#     dict = {}
#     for i in range(1,n+1):
#         dict[i] = i*i
#     print(dict)
# printDict()

# # 73
# n = int(input("Enter an integer"))
# ans = 0
# while n>0:
#     i = n%10
#     ans += i
#     n //= 10
# print(ans)

# # 74
# def print_prime(n):
#     for num in range(2, n + 1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
# print_prime(25)

# # 75
# def rec(n):
#     if n <= 0:
#         return
#     print(n)
#     n -= 1
#     rec(n)

# x=int(input("Enter the number: "))
# rec(x)