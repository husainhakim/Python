sparshva=[]
times=int(input("Enter the number of elements in the lists:-"))
i=1
for i in range(i,times+1):
 
   sparshva.append(int(input("Enter the  element:-")))
print(sparshva)

max=sparshva[0]
for num in sparshva:
     if num > max:
      max=num
min=sparshva[0]
for num in sparshva:
    if num <min:
     min=num
print("The smallest item in the list is",min)
print ("The largest in the list is",max)
