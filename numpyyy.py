from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import os.path

# 26
# arr = np.ones(5)
# print(arr)


#27
# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15],
#                 [16, 17, 18, 19, 20]
#                    ])
# print(arr)
# print([1, 2, 3, 4, 5] in arr.tolist())
# print([16, 17, 20, 19, 18] in arr.tolist())

# # 28
# mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
# mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])

# res = np.dot(mat1,mat2)
# print(res)
# res = np.add(mat1,mat2)
# print(res)

# # 29
# arr = np.array([1,1,1,2,3,])
# print(np.bincount(arr).argmax())

# # 30
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# arr = arr.flatten()
# print(arr)

# # 31
# num = np.arange(36) #creates a array with 36 elements from 0-35
# arr1 = np.reshape(num, [4, 9])  #reshaping to 4 rows and 9 columns
# print("Original array:")
# print(arr1)
# result  = arr1.sum(axis=0)   #adding columns because axis=0
# print("\nSum of all columns:")
# print(result)

# # 32
# arr = np.array([1,2,3,4,5])
# print(arr.mean())
# print(arr.std())
# print(arr.var())

# # 33
# x = np.array(["Python","is","not","easy"])
# print(x)
# r = np.char.join(" ",x)
# print(r)

# 34
# x = np.array([1,2,3,4,5])
# plt.plot(x,x)
# plt.show()

# # 81
# arrc = np.array([1, 2, 3, 4, 5])  #elements in celcius
# arrf=np.array([33.8,35.6,37.4,39.2,41.0])  #same elemnts in fahrenhiet
# arr2 = arrc*1.8 + 32  #converting to fahrenhiet
# print(arr2)
# arr3 = (arrf-32)*5/9  #reconverting to celcius
# print(arr3)

# # # 82
# arr1 = np.array([4,3,2,1])
# arr2 = np.array([6,5,4,3])
# arr3 = np.setdiff1d(arr1,arr2)
# print(arr3)