#reverse, summation, pythago, sorting ,pattern

# #35
# num = 1345
# revnum = 0
# while num>0:
#     temp = num%10
#     revnum = revnum*10 + temp
#     num //= 10
# print(revnum)

# # 36
# number = int(input("Enter the Natural Number: "))
# for j in range(1, number+1):
#     num = 0
#     for i in range(1, j+1):
#         print(i, sep=" ", end=" ")
#         if(i < j):
#             print("+", sep=" ", end=" ")
#         num += i
#     print("=", num)

# # 37
# limit = 30   #maxm value for hypotenuse of pythago triplets
# c = 0  #counter variable tokeep track of generated triplets
# m = 2  #starting value for one of the legs of the triplets
# while c<limit:
#     for n in range(1,m):
#         a = m*m - n*n
#         b = 2*m*n
#         c = m*m + n*n
#         if(c>limit):
#             break
#         print(a,b,c)
#     m = m+1

# # 38
# num = 101111
# str = str(num)
# zeros = 0
# ones = 0
# for i in range (len(str)):
#     if(str[i] == '0'):
#         zeros += 1
#     else:
#         ones += 1
# if(zeros == 1 or ones == 1):
#     print("YES")
# else:
#     print("NO")

# # 39
# l=list(map(int,input().split(" ")))
# print(l)
# c=0
# y=0
# while y < len(l)-1:
#     min=l[y]
#     val=l[y]
#     for x in range(y+1, len(l)):
#         val=l[x]
#         if val < min:
#             break
#     if val < min:
#         l.remove(min) 
#         l.append(min)
#         c=c+1
#     else:
#         y=y+1
# print(c)

# 40
# x=int(input("Enter a nummber: "))
# for i in range (1,x):
#     for j in range(1,i+1):
#         print(i,end = "")
#     print("")


# # 42
# inp = int(input("Enter a number: "))
# c= 0
# while inp>=10:
#     inp //= 6
#     c+=1
# print(c)