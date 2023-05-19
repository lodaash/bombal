import random
import math

# 4
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {**dic1, **dic2, **dic3}
print(dic4)

# 5
i = 4
if i in dic4:
    print(i," is present")
else:
    print(i," is not present")


# 6
dic5 = {}

for i in range(1,6):
    dic5[i] = i*i
print(dic5)


# 7
dic5.pop(3)
print(dic5)


# 8
l1 = [1,2,3,4]
l2 = [5,6,7,8]
dic6 = dict(zip(l1,l2))
print(dic6)


#9
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)

s = set()
for dic in L:
    for val in dic.values():
        s.add(val)
print("Unique Values: ",s)


#10
str1 = 'pythonprac' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1  #get use karne ne default value daal sakte hai , warna error aata
print(my_dict)


# 13
dict = {"Afghanistan":"Afghani","Luxembourg ":"Euro","Qatar":"Qatari Riyal","Vietnam":"Dong","India":"Rupee"}
for i,j in dict.items():
    print(i,":",j)

# 23
dict = {
    "state1":"cap1",
    "state2":"cap2",
    "state3":"cap3",
    "state4":"cap4",
}
dict["state5"] = "cap5"
print(dict)

#  41
key = [1,2,3,4,5]
val = ['a','b','c','d','e']
my_dict = {}
for i in range(0,len(key)):
    my_dict[key[i]] = val[i]
print(my_dict)
res = dict(zip(key, val))
print(res)