# dictionaries=key-value pair
d={1:"sparshva is noob",'two':42,'noobpro':"nigga",'hi noob':(1,2,3,'hi brother'),'gaurang':{'hi':'hello','noob':23}}
print(d)
print(d[1])
print(d['noobpro'])
print(d['two'])
print(d['hi noob'])
print(d['gaurang'])
del(d[1])
print(d)
del(d['gaurang']['hi'])#how to delete an element in an inner dictionary 
print(d)