#wapp to print the index at which the particular value exists , if the value exists at multiple locations in the list use mutiple indices,also count the number of times the particular values is repeated int the list
numberelements=int(input("Enter number of elements:- "))
sparshva=[]
count=0
for i in range(numberelements):
    elements=int(input("Enter element:-"))
    sparshva.append(elements)
print(sparshva)
b=int(input("Enter element to search for:-"))
for i in range(numberelements):
    if sparshva[i]==b:
        count+=1
        print("Position(Index):-",i)
print("Repeated time(Count):-",count)
