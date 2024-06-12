d={1:'hello','two':42,'blah':[1,2,3]}
print(d.keys())
print(d.values())
# print(d.clear())
d2={34:'hi noob'}
d.update(d2)
print(d)
d.pop(1)
print(d)