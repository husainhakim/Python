# ,Wap for accessing elements from a dictionary.     i/p: r1={'id':101,'name':'Amit','Age':21}

#   a. By using key name.
#   b. By using get() method.

r1={'id':101,'name':'Amit','Age':21}
print("Accessing elements using key name:")
print("ID:", r1['id'])
print("Name:", r1['name'])
print("Age:", r1['Age'])
print("Accessing elements using get() method:")
print("ID:", r1.get('id'))
print("Name:", r1.get('name'))
print("Age:", r1.get('Age'))
print("Accessing a key that doesn't exist using get() with a default value:")
print("Gender:", r1.get('Gender', 'Not specified'))