
#wap to remove an empty tuple from a list of tuples
a=[(),(),(","),("a","b"),("a","b","c"),("d")]
a=[i for i in a if i!=()] #list comprehension
print(a)