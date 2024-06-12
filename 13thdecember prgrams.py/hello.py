vowel = ["A","E","I","O","U"]

a = input("Enter the word : ")

count = 0

for i in a:
    if i.upper() in vowel:
        count+=1
    
print(count)
