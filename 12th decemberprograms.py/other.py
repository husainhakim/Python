# import math
# def dist ( x1,x2,y1,y2):
#     distx1 = abs(x1-x2)
#     distx2 = abs(y1-y2)

#     distance = math.sqrt((distx1*distx1) + (distx2*distx2))
#     return distance

# print(dist(45,43,66,72))
def distance(x1,x2,y1,y2):
    print((((x2-x1)*2)+((y2-y1)*2))*0.5)
distance(1,4,2,6)