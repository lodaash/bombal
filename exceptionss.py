# # 53
# class InvalidMarks(Exception):
#     pass
# while True:
#     try:
#         marks = int(input("Enter your marks"))
#         if marks > 100:
#             raise InvalidMarks
#         else:
#             print(marks)
#             break
#     except InvalidMarks:
#         print("Please enter marks below 100")

# # 54
# class ZeroDivisionError(Exception):
#     pass
# a = 1
# b= 2
# c = 3
# d = 0
# try:
#     if b*d == 0:
#         raise ZeroDivisionError
#     ans =  ((a+d) + (b*c))/ (b*d)
#     print(ans)
# except ZeroDivisionError:
#     print("b*d ie the denominator turns out to be 0")

# # 55
# class InvalidAge(Exception):
#     pass
# try:
#     age = int(input("Enter your age"))
#     if age<18:
#         raise InvalidAge
#     print("Age is valid")
# except InvalidAge:
#     print("Age is not valid")

# # 56
# try:
#     f = open("temp5.txt",'r')
#     print("file found")
# except FileNotFoundError:
#     print("File not found")

##57
# x = "ev"
# try:
#     if not (type(x)== str):
#         raise TypeError
# except TypeError:
#     print("Enter a string"