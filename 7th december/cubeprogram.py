
list = [int(i) for i in input("Enter num : ").split()] 

for i in range(0,len(list)) :
    a = list[i]**3
    t = (list[i],a)
    list.remove(list[i])
    list.insert(i,t)

print(list)

