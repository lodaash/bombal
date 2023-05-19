import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# # 67
# data = {'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
#  'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
#  'age': [41, 28, 33, 34, 38, 31, 37],
#  'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
#  }

# f1=pd.DataFrame(data)

# print(f1)

# x=data["name"]
# y=data["age"]

# plt.plot(x,y)
# plt.show()



exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

newdf = pd.DataFrame(exam_data,index=labels)

# 83
# print(newdf)

# #84
# print(newdf.head(3))

## 85
# print(newdf.loc[:,['name','score']])
# print(newdf[['name','score']])

## 86
# print(newdf.iloc[[1, 3, 5, 6], [1, 3]])

## 87
# print(newdf[newdf['attempts'] > 2])

## 88
# rows = len(newdf)
# col = len(newdf.axes[1])
# print("rows:", rows)
# print("col:", col)

## 89
# print(newdf[newdf['score'].between(15, 20)])

## 90
# print(newdf[(newdf['attempts'] < 2) & (newdf['score'] > 15)])


## 91
# newdf.loc['k'] = [ 'Suresh', 15.5,1, 'yes']
# print(newdf)
# newdf = newdf.drop('k')
# print(newdf)

## 92
# df = newdf.sort_values(by=['name'], ascending=[False])
# print(df)
# df = newdf.sort_values(by=['score'], ascending=[True])
# print(df)

#J
# df = newdf.sort_values(by=['name', 'score'], ascending=[False, True])
# print(df)


# # 93
# newdf['qualify'] = newdf['qualify'].map({'yes': True, 'no': False})
# print(newdf)


# # 94
# print(newdf)
# newdf._set_value('h', 'score', 20)
# newdf.at['h','score'] = 20   #better and more preferred
# print(newdf)