a = input("Enter  : ").split(" ")
for i in range(0,len(a)):
    str1 = ""
    for j in range(0,len(a[i])):
        
        if(a[i][j] == a[i][j].upper()):
            if(j == 0):
                str1 += a[i][j]
            else:
                str1 += a[i][j].lower()
        else:
            str1 += a[i][j]
    a[i] = str1
for i in a:
    print(i,end=" ")