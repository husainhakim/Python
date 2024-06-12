#WAP sum and mean of elements in a list
list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range (len(list)):
    sum=sum+list[i]
print(sum)
mean=sum//10
print(mean)