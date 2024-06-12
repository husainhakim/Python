# wap to unzip a list of tuples into indivisual lists
#WAP to unzip a list of tuple into individual list
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
unzip = list(zip(*my_list))
x = [list(elem) for elem in unzip]
print(x)
