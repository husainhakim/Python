
# def QuestionsMarks(str):
#     a = 11
#     b = 'false'
#     c = 0
#     for i in str:
#         if i.isdigit():
#             if int(i) + a == 10:
#                 if c != 3:
#                     return 'false'
#                 b = 'true'
#             c = 0
#             a = int(i)
#         elif i == '?':
#             c += 1
#     return b
# # keep this function call here
# z = 'acc?7??sss?3rr1??????'
# print(QuestionsMarks(z))


# def FirstFactorial(num):
#   if num ==1:
#     return 1
#   else:
#     return num * FirstFactorial(num-1)
#   # code goes here

# # keep this function call here 
# print(FirstFactorial(4)) 
# def FirstReverse(strParam):
#  a = strParam[::-1]
#  return a
# # code goes here
  

# keep this function call here 

# def FirstReverse(str):
#   a=str[::-1]
#   return a
# print(FirstReverse(input()))

# def Firstfactorial(num):
#   if num==1:
#     return 1
#   else:
#     return num*Firstfactorial(num-1)
# print(Firstfactorial(int(input())))

# def Firstreverse(sen):
#   nw=""
#   for letter in sen:
#     if letter.isalpha() or letter.isnumeric():
#       nw+=letter
#     else:
#       nw+=" "
#   return max(nw.split(),key=len)
# print(Firstreverse(input()))

# def firstreverse(word):
#    a=word[::-1]
#    return a
# print(firstreverse(int(input())))


# def FirstReverse(str):
#   a=str[::-1]
#   return a
# print(FirstReverse(input()))
a=lambda b:b+10

result=a(int(input()))
print(result)

a = lambda a: a + 10
result = a(int(input("Enter a number: ")))
print("Result is:", result)
