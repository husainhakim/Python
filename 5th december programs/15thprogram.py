list=[11,22,33,44,55]
even=[]
odd=[]
for i in range(len(list)):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])
print(list)
print('Even:-',even)
print('Odd:-',odd)