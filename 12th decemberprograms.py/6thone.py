 
#  i/p={ }  

#  o/p={0: 'Amit', 1: 'Kumar', 2: 23, 3: 'Delhi', 'marks': (69, 70, 58), 4: {'Nested': {'Name': 'Shivang', 'Age': 24}}}

#   1. Adding one element at a time.
#   2. Adding multiple values to a key.
#   3. Updating an existing Key's Value. 
#   4. Adding Nested Key value.
dictionary = {0:'Amit',1:'Kumar',2:23,3:'Delhi'}
print(dictionary)
dictionary['marks'] = (69, 70, 58)
print(dictionary)
dictionary[2] = 25  
print(dictionary)
dictionary[4] = {'Nested': {'Name': 'Shivang', 'Age': 24}}
print(dictionary)
