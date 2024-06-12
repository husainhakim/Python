n=int(input("Enter number of elements:-"))
list=[]
list1=[]
for i in range(n):
    a=input("Enter word:-")
    list.append(a)
print(list)
for i in range(n):
    list1.append(list[i][0])
print(list1)