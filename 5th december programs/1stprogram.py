
# Aim: to demonstrate methods of list 
x=['sparshva','faheem don','gauri','chaitu','chikne']# L.append():adds item 
x.append('king')
print(x)
x.extend(['dalvia','lakshya bhai','jeevan the naidu'])# L.extend():adds mutiple items
print(x)
x.pop(2)#Remove item i from the list.defaut last
print(x)
x.reverse()#reverse the order of items in list
print(x)
x.insert(1,'areeb king')#inserts item at position i 
print(x)
x.remove('dalvia')#fins item in list and deletes it from the list 
print(x)
x.sort(reverse=True)#sorts the list in descending order
print(x)
x.sort(reverse=False)#sorts the list in ascending order
print(x)