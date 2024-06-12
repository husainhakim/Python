#3.write a program arrange lists in descending order
a = [10,2,3,4,50,832,7]
# a.sort(reverse = True)
# print(a)

b=0
c=len(a)-1
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]<a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)