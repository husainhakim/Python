from colorama import Fore
import time
class BikeShowroom:
    def __init__(self):
        self.bikes = {
            "royal enfield": [
                {"model": "Royal Enfield Classic 350", "price": 180000},
                {"model": "Royal Enfield Bullet 350", "price": 150000},
                {"model": "Royal Enfield Meteor 350", "price": 200000},
                {"model": "Royal Enfield Himalayan", "price": 220000},
                {"model": "Royal Enfield Continental GT 650", "price": 300000}
            ],
            "harley davidson": [
                {"model": "Harley Davidson Street 750", "price": 550000},
                {"model": "Harley Davidson Iron 883", "price": 750000},
                {"model": "Harley Davidson Fat Boy", "price": 1200000},
                {"model": "Harley Davidson Forty-Eight", "price": 900000},
                {"model": "Harley Davidson Road Glide Special", "price": 1500000}
            ],
            "yamaha": [
                {"model": "Yamaha YZF R15 V4", "price": 180000},
                {"model": "Yamaha FZS-FI", "price": 120000},
                {"model": "Yamaha MT-15", "price": 150000},
                {"model": "Yamaha Fascino 125", "price": 70000},
                {"model": "Yamaha FZ-X", "price": 110000}
            ],
            "bajaj": [
                {"model": "Bajaj Pulsar 150", "price": 90000},
                {"model": "Bajaj Dominar 400", "price": 190000},
                {"model": "Bajaj Avenger Cruise 220", "price": 120000},
                {"model": "Bajaj Platina 110", "price": 60000},
                {"model": "Bajaj CT 100", "price": 45000}
            ]
        }

    def display_bikes_by_company(self, company):
        if company in self.bikes:
            print(f"{Fore.CYAN}Bikes from {company.title()}:{Fore.RESET}")
            for index, bike in enumerate(self.bikes[company], start=1):
                print(f"{Fore.GREEN}{index}. {bike['model']} - Price: {bike['price']}{Fore.RESET}")
            return self.bikes[company]
        else:
            print("Company not found in the showroom.")
            return []

    def choose_bike(self, bikes):
        while True:
            bike_choice = int(input(f"{Fore.LIGHTMAGENTA_EX}Choose the bike number you want to buy (Enter 0 to exit): {Fore.RESET}"))
            if bike_choice == 0:
                break
            elif 1 <= bike_choice <= len(bikes):
                selected_bike = bikes[bike_choice - 1]
                print(f"You have selected: {Fore.GREEN}{selected_bike['model']} - Price: {selected_bike['price']}{Fore.RESET}")
            else:
                print("Invalid bike number selected. Please try again.")

    def display_bikes_under_budget(self, budget):
        print(f"{Fore.CYAN}Bikes under budget {budget}:{Fore.RESET}")
        for company, bikes in self.bikes.items():
            for bike in bikes:
                if budget == 1 and bike["price"] <= 100000:
                    print(f"{Fore.GREEN}{bike['model']} - Price: {bike['price']}{Fore.RESET}")
                elif budget == 2 and 100000 < bike["price"] <= 200000:
                    print(f"{Fore.GREEN}{bike['model']} - Price: {bike['price']}{Fore.RESET}")
                elif budget == 3 and 200000 < bike["price"] <= 500000:
                    print(f"{Fore.GREEN}{bike['model']} - Price: {bike['price']}{Fore.RESET}")
                elif budget == 4:
                    print(f"{Fore.GREEN}{bike['model']} - Price: {bike['price']}{Fore.RESET}")

    
    def welcome_message(self):
        while True:
            print(f'{Fore.BLUE}{"-"*20}Welcome to our bike showroom{"-"*20}{Fore.RESET}\nHow can I help you today?\n1) Display all bikes\t\t2) Buy a bike\n3) Rent a bike\t\t\t4) Loan a bike\n5) Exit\n{Fore.LIGHTYELLOW_EX}Enter the number corresponding to the option (1-5):{Fore.RESET}')
            ask = int(input())
            if ask == 5:
                print("Thanks for visiting, have a great day ahead!")
                break
            elif ask == 2 or ask == 3 or ask == 4:
                ask_about_bike = int(input(f"{Fore.LIGHTMAGENTA_EX}Are you looking for any certain bike you have decided or are you looking to buy/rent?{Fore.RESET}\n1) Looking for my favorite bike\n2) Any bike that is good is fine\nEnter the number corresponding to the option(1-2):"))
                if ask_about_bike == 1:
                    ask_about_company = (input(f"Which company's bike are you looking for?\n1) Royal Enfield\t\t2) Harley Davidson\n3) Yamaha\t\t\t4) Bajaj\n{Fore.CYAN}Enter the name of the company(string):{Fore.RESET} ")).lower()
                    bikes = self.display_bikes_by_company(ask_about_company)
                    if bikes:
                        self.choose_bike(bikes)
                elif ask_about_bike == 2:
                    ask_about_budget = int(input(f"What is the budget under which you are looking for a bike?\n1) Under 1 lakh\t\t2) Under 2 lakh\n3) Under 5 lakh\t\t4) There is no limit for the budget\n{Fore.LIGHTRED_EX}Enter the number corresponding to your option:{Fore.RESET} "))
                    self.display_bikes_under_budget(ask_about_budget)
                    askaboutbike = input("Enter the name of the bike you want to buy: ")
                    found = False
                    for company, bikes in self.bikes.items():
                        for bike in bikes:
                            if bike["model"].lower() == askaboutbike.lower() and bike["price"] <= ask_about_budget * 100000:
                                found = True
                                print(f"To confirm the order of {askaboutbike}, please fill this form:\n")
                                name = input("Enter your name: ")
                                age = int(input("Enter your age: "))
                                if age < 18:
                                    print("Sorry, you must be 18 or older to make a purchase.")
                                    break
                                email = input("Enter your email id: ")
                                if '@' not in email:
                                    print("Invalid email")
                                    break
                                print("Order confirmed! Thank you for shopping with us.")
                    if not found:
                        print(f"{askaboutbike} not found within the budget or company.")

showroom = BikeShowroom()
showroom.welcome_message()