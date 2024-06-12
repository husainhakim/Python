# a="Itm skills university"
# print(type(a))

# print(a[0])
# print(a[:-1])
# print(a[::-1])
# print(a[:21])
# print(a[0:18])
# print(a[-21::+1])
# for i in range (len(a)):
#     print(a[i])
# i=0  
# while i<len(a):
#     print(a[i])
#     i+=1
# i = 0
# # while(i<21):
# #     print(a[i])
# #     i+=1
# def search(a,b):
#     count=0
#     for i in range(0,len(a)):
#         if b == a[i]:
#             count+=1
#     return count

# a= input("enter the word :-") 
# b = input("enter the element to search :-")
# index = search(a , b)
# # print(index) if b in a else print(b,"is not in the word")
# print(f"Number of times repeated:-{index}")
# hi=input("Enter the word:-")
# hello=input("Enter the element to search:-")
# print(hi.find(hello))
# if hello in hi:
#     print(f"{hello} is in {hi}")
# else:
#     print("Not in hi")\
def find(a,b):
    if b in a:
        for i in range(0,len(a)):
            flag = 0
            if(b[0] == a[i]):
                for j in range(0,len(b)):
                    if(not(a[i+j]==b[j])):
                        flag = 0
                        break
                    flag = 1
            if(flag == 1 ):
                return i
            
    else:
        return "None"
        
        

a= input("enter the word : ") 
b = input("enter the element to search : ")
i = find(a , b)
print(f"{i} to {i+len(b)-1}")
