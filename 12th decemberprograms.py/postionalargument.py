# rafe=(1,2,3,4,5,5,6,100)


# def sparshva(*rafe):
#   for i in rafe:
#       sum=sum+i
#       return sum
# hihello=sparshva(*rafe)
# print(hihello)
# rafe = (1, 2, 3, 4, 5, 5, 6, 100)

# def sparshva(*rafe):
#     sum = 0  
#     for i in rafe:
#         sum += i  
#     return sum  


# result = sparshva(*rafe)
# print("The sum of elements in tuple is:", result)
def main():
    a = 10
    b = 55
    result = abs(a,b)
    print("absolute value of ",a,"-",b,"=",result)
    print("dir in main()",dir())

def abs(x,y): 
    print("in function absdiff dir()",dir())
    z = y-x
    return z
main() 