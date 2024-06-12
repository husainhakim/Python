#wap to create a dictionary with mixed keys,and prnt key values and key value pairs

dict = {1: "India", 'city': 'New Delhi', 'Record': {'id': 101, 'name': 'Amit', 'age': 21}}
print("Keys:-")
for key in dict.keys():
    print(key)


print("Values:-")
for value in dict.values():
    print(value)


print("Key-Value Pairs:-")
for key, value in dict.items():
     print(key,value)