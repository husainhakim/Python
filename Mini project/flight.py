from colorama import Fore

import time
class Flight():
    def flight(self):
     flightno="A490292011"
     self.seatlist=[]
     print(f"{Fore.CYAN}{'-'*20}Welcome to our ITM airlines{'-'*20}{Fore.RESET}")
     while True:
   
      self.ask=int(input(f"How can we help you today?\n1)Book a ticket\n2)Cancel a ticket\n3)Find details about flight\n{Fore.GREEN}Enter the number coresponding to the option(1-3):{Fore.RESET}"))
      if self.ask==1:
        self.pickup=input("Enter the pickup point:-").upper()
        self.destination=input("Enter the destination:-").upper()
        if self.pickup==self.destination:
            print("The pickup point and destination cannot be the same")
            break
        self.askclass=int(input("Enter the class you would like to travel in\n1)Economy\n2)Business\nEnter the number coresponding to the option:"))
        self.distance=int(input("Enter the distance from from pickup point to destination:"))
        self.nooftickets=int(input("Enter the number of tickets you want:"))
        for i in range(self.nooftickets):
            self.seatno = int(input(f"Enter the seat no. for passenger no. {i+1}: "))
        if self.seatno>150:
            print("Invalid seat no.")
        elif self.seatno in self.seatlist:
            print("Seat has already been booked")
        else:
            self.seatlist.append(self.seatno)
            self.name=input("Enter name:")
            self.pickupdate=input("Enter the pickupdate:")
            print("Generating a ticket! please standby")
            time.sleep(3)
            if self.askclass==1:
                price=self.nooftickets*10*self.distance
            elif self.askclass==2:
                price=self.nooftickets*20*self.distance
            print("Name\t|\tpickup\t|\tdestination\t|\tNo.of tickets")
            print(self.name,"\t|\t",self.pickup,"\t|\t",self.destination,'\t|\t',self.nooftickets)
husain=Flight()
husain.flight()


