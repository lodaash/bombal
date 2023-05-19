from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import os.path


# # 43
# with open("temp.txt",'r') as f:
#     for line in f:
#         print(line.title())
# f.close

# # 44
# with open("temp.txt",'r') as f:
#     dict = {}
#     for line in f:
#         for letter in line:
#             dict[letter] = dict.get(letter,0) +1
#     print(dict)
# f.close() 

# # 45
# part 1
# with open("temp.txt",'w') as f:   #overwrites existing content
#     f.write("HELLO WORLD")
#     f.close()
# with open("temp.txt",'r') as f:
#     print(f.read())

# part 2
# with open("temp.txt",'a') as f:  #appends content
#     f.write("I am a rookie python programmer")
#     f.close()
# with open("temp.txt",'r') as f:
#     print(f.read())

# # 47
# f2 = open("temp2.txt",'a')
# f = open("temp.txt",'r')
# cont  = f.read()
# f2.write(cont)

# # 48
# f = open("temp2.txt",'a')
# n = int(input("Enter the number of students: "))
# for i in range(0,n):
#     name = input("Enter the name of the student: ")
#     roll = input("Enter the roll number of the student: ")
#     str = name+":"+roll
#     f.write(str)
#     f.write("\n")
# f.close()
# path = "temp2.txt"
# isExist = os.path.exists(path)
# print(isExist)

# # 49
# file1 = input("Enter the first file :")
# file2 = input("Enter the second file :")
# f2 = open(file2,'a')
# with open(file1,'r') as f:
#     for line in f:
#         f2.write(line)

# # 50
# f = open("temp.txt",'r')
# for line in f:
#     list = line.split(" ")
#     for i in list:
#         print(i)

# # 51
# f = open("temp.txt",'r')
# for line in f:
#     for char in line:
#         print(char)

# # 52
# char = 0
# word = 0
# lines = 0
# space=0
# f = open("temp.txt",'r')
# for line in f:
#     lines  = lines + 1
#     list = line.split(" ")
#     word = word + len(list)
#     for chars in line:
#         char = char + 1
#         if chars == " ":  # Check if the character is a space
#             space += 1 
# print(char)
# print(word)
# print(lines)
# print(space)