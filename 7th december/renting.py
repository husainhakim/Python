print("--------------Hello and welcome to sparshva  parking lot-----------------")
# time=eval(input("Enter the checkout time as 24 hours watch and put '.'a dot in the middle '-' put a minus sign in the middle and then put check in time:-"))
# print(time)

name=input("Enter your name:-")
carname=input("Enter the name of your vehicle:-")
checkintime=float(input("Enter the check-in time:-"))
checkouttime=float(input("Enter the checkout-time:-"))
hours=int(checkouttime-checkintime)
typeofcar=input("What is the type of the vehicle?\nType:\n1)'C' for car\t\t2)'B' for bus\n3)'R' for Rickshaw\t4)'H' for bike\n5)'T'for Truck\t\t6)'O' for others\n")
if hours <3 :
        if typeofcar.upper()=="C":
            print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
            print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',100*hours,'\t|\t',carname)
        elif typeofcar.upper()=="B":
               print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
               print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',150*hours,'\t|\t',carname)
        elif typeofcar.upper()=="R":
            print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
            print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',70*hours,'\t|\t',carname)
        elif typeofcar.upper()=="H":
         print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
         print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',50*hours,'\t|\t',carname)
        elif typeofcar.upper()=="T":
            print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
            print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',200*hours,'\t|\t',carname)
        elif typeofcar.upper()=="O":
         print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
         print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',100*hours,'\t|\t',carname)
        else:
         print("Invalid input please try again")
elif hours>=3:
    if typeofcar.upper()=="C":
           print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
           print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',120*hours,'\t|\t',carname)
    elif typeofcar.upper()=="B":
           print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
           print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',70*hours,'\t|\t',carname)
    elif typeofcar.upper()=="R":
         print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
         print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',100*hours,'\t|\t',carname)
    elif typeofcar.upper()=="H":
        print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
        print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',80*hours,'\t|\t',carname)
    elif typeofcar.upper()=="T":
       print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
       print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',250*hours,'\t|\t',carname)
    elif typeofcar.upper()=="O":
        print('Name\t|\tCheckin\t|\tCheckout\t|\tHours\t|\tRent\t|\tVehicle name')
        print(name,'\t|\t',checkintime,'\t|\t',checkouttime,'\t\t|\t',hours,'\t|\t',120*hours,'\t|\t',carname)
    else:
         print("Invalid input please try again")
