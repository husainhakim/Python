# Wap to generate & print dictionary of no & its square like(i,i*i).
#    eg {1:1, 2:4, 3:9....}
n =int(input("Enter the number:-"))
squaredict = {i: i*i for i in range(1, n+1)}

print(squaredict)

