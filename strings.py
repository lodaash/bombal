# # 11
# string = input("Enter a sentence: ") 
# newstr = string.replace(" ","-") 
# print(newstr)

# #12
# rno = min(random.sample(range(100, 200), 10))
# print(rno)

# #14
# comnum = 3+2j
# comnum2 = complex(3,2)
# print(type(comnum))
# print(comnum.real)
# print(comnum.imag)
# print(comnum.conjugate())
# def magnitude(comnum):
#     r = comnum.real
#     i = comnum.imag
#     ans = r*r + i*i
#     return math.sqrt(ans)
# print(magnitude(comnum))

# #15
# str = "   hello"
# str = str.lstrip()
# str = str.replace("llo","lp")
# print(str)

# #17
# str = "firstandlast"
# strnew = str[-1:] + str[1:-1] + str[:1]
# print(strnew)

# #18
# str = "ispresent"
# if "present" in str:
#     print("present is present")
# else:
#     print("present is not present")

# #20
# str = "biggib"
# revstr = reversed(str)
# if list(str) == list(revstr):
#     print(True)
# else:
#     print(False)

# # 21
# str = "hello world"
# str = str.title()
# print(str)

# #22
# str = "hello world"
# map = {}
# for i in str:
#     map[i] = map.get(i,0) +1 
# print(map)


# #24 ----> with predefined
# def count_characters(sentence):
#     digit_count = 0
#     symbol_count = 0
#     vowel_count = 0
#     consonant_count = 0

#     vowels = 'aeiou'
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

#     for char in sentence:
#         if char.isdigit():
#             digit_count += 1
#         elif char in symbols:
#             symbol_count += 1
#         elif char.isalpha():
#             if char.lower() in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1

#     return digit_count, symbol_count, vowel_count, consonant_count

# # Test the function
# sentence = input("Enter a sentence: ")
# digits, symbols, vowels, consonants = count_characters(sentence)

# print("Number of digits:", digits)
# print("Number of special symbols:", symbols)
# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)

# #24 ----> without predefined
# def countCharacterType(str):
#     vowels = 0
#     consonant = 0
#     specialChar = 0
#     digit = 0

#     for i in range(0, len(str)):
         
#         ch = str[i]
 
#         if ( (ch >= 'a' and ch <= 'z') or
#              (ch >= 'A' and ch <= 'Z') ):
 
#             ch = ch.lower()
 
#             if (ch == 'a' or ch == 'e' or ch == 'i'
#                         or ch == 'o' or ch == 'u'):
#                 vowels += 1
#             else:
#                 consonant += 1
         
#         elif (ch >= '0' and ch <= '9'):
#             digit += 1
#         else:
#             specialChar += 1
     
#     print("Vowels:", vowels)
#     print("Consonant:", consonant)
#     print("Digit:", digit)
#     print("Special Character:", specialChar)
# str = "Password23@#"
# countCharacterType(str)

# # 25
# str = input("Enter a string with less then 15 letter: ")
# if(len(str)>15):
#     print("Enter a string with less characters")
# else:
#     for i in range(len(str)):
#         print(i,":",str[i])