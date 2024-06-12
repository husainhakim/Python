# from colorama import Fore
# from bikes_and_banks import RoyalEnfieldShowroom

# class UserInput:
#     def get_user_input(self):
#         showroom = RoyalEnfieldShowroom()
#         print(f"{Fore.GREEN}{'-'*20}Welcome to Royal Enfield Showroom!{'-'*20}{Fore.RESET}")
#         want_bike = input("\n\nWelcome to Royal Enfield Showroom! Do you want to buy a bike? (yes/no): ")
#         if want_bike.lower() != 'yes':
#             print("Thanks for visiting!")
#             return

#         print("Choose a bike:")
#         for key, value in showroom.bikes.items():
#             print(f"{key}: {value[0]} - Price: {value[1]}")

#         bike_choice = int(input("Enter the number corresponding to the bike you want: "))
#         selected_bike = showroom.bikes.get(bike_choice)
#         if not selected_bike:
#             print("Invalid choice!")
#             return

#         print(f"Please fill this form to confirm the order of your {selected_bike[0]}:")
#         name = input("Name: ")
#         age = int(input("Age: "))
#         if age < 21:
#             print("Underage to buy a bike")
#             return

#         address = input("Address: ")
#         email = input("Email Address: ")
#         financial_proof = input("Financial Proof (e.g., bank statement, salary slip): ")

#         bike_price = selected_bike[1]
#         want_loan = input("Do you want a loan? (yes/no): ")

#         user_input_data = {
#             "bike_price": bike_price,
#             "selected_bike": selected_bike,
#             "name": name,
#             "age": age,
#             "address": address,
#             "email": email,
#             "financial_proof": financial_proof,
#             "want_loan": want_loan
#         }

#         return user_input_data

# from bikes_and_banks import RoyalEnfieldShowroom

# class UserInput:
#     @staticmethod
#     def get_user_input():
#         showroom = RoyalEnfieldShowroom()
#         print(f"{'-' * 20} Welcome to Royal Enfield Showroom! {'-' * 20}")

#         want_bike = input("Do you want to buy a bike? (yes/no): ")
#         if want_bike.lower() != 'yes':
#             print("Thanks for visiting!")
#             return

#         print("Choose a bike:")
#         for key, value in showroom.bikes.items():
#             print(f"{key}: {value[0]} - Price: {value[1]}")

#         bike_choice = int(input("Enter the number corresponding to the bike you want: "))
#         selected_bike = showroom.bikes.get(bike_choice)
#         if not selected_bike:
#             print("Invalid choice!")
#             return

#         print(f"Please fill this form to confirm the order of your {selected_bike[0]}:")
#         name = input("Name: ")
#         age = int(input("Age: "))
#         if age < 21:
#             print("Underage to buy a bike")
#             return

#         address = input("Address: ")
#         email = input("Email Address: ")
#         financial_proof = input("Financial Proof (e.g., bank statement, salary slip): ")

#         want_loan = input("Do you want a loan? (yes/no): ")

#         return {
#             'selected_bike': selected_bike,
#             'name': name,
#             'age': age,
#             'address': address,
#             'email': email,
#             'financial_proof': financial_proof,
#             'want_loan': want_loan
#         }


# from loan_process import BikeLoan

# class UserInput:
    
#     def get_loan_details():
#         principal = float(input("Enter the loan amount: "))
#         time = int(input("Enter the loan duration in months: "))
#         return principal, time

    
#     def get_bank_details(banks):
#         print("Available Banks:\n")
#         for bank in banks:
#             print(bank)

#         selected_bank = input("Enter the name of the bank: ")
#         if selected_bank not in banks:
#             print("Invalid bank selection. Exiting.")
#             return None
#         return selected_bank

    
#     def create_loan():
#         banks = {
#             "SBI": 8.5, 
#             "ICICI BANK": 9.0,
#             "YES BANK": 9.5
#         }

#         selected_bank = UserInput.get_bank_details(banks)
#         if selected_bank is None:
#             return None

#         rate = banks[selected_bank]
#         principal, time = UserInput.get_loan_details()
#         bike_loan = BikeLoan(principal, rate, time)
#         return bike_loan



# from loan_process import BikeLoan

# class UserInput:
    
#     def get_user_input(self):
#         principal = float(input("Enter the loan amount: "))
#         time = int(input("Enter the loan duration in months: "))
#         return principal, time

    
#     def get_bank_details(self, banks):
#         print("Available Banks:\n")
#         for bank in banks:
#             print(bank)

#         selected_bank = input("Enter the name of the bank: ")
#         if selected_bank not in banks:
#             print("Invalid bank selection. Exiting.")
#             return None
#         return selected_bank

    
#     def create_loan(self):
#         banks = {
#             "SBI": 8.5, 
#             "ICICI BANK": 9.0,
#             "YES BANK": 9.5
#         }

#         selected_bank = self.get_bank_details(banks)
#         if selected_bank is None:
#             return None

#         rate = banks[selected_bank]
#         principal, time = self.get_loan_details()
#         bike_loan = BikeLoan(principal, rate, time)
#         return bike_loan
# from bikes_and_banks import RoyalEnfieldShowroom

# class UserInput:
#     def select_bike(self):
#         showroom = RoyalEnfieldShowroom()
#         print("Available Bikes:")
#         for key, value in showroom.bikes.items():
#             print(f"{key}: {value[0]} - Price: {value[1]}")

#         bike_choice = int(input("Enter the number corresponding to the bike you want: "))
#         selected_bike = showroom.bikes.get(bike_choice)
#         if not selected_bike:
#             print("Invalid choice!")
#             return None

#         return selected_bike

#     def get_user_details(self):
#         name = input("Enter your name: ")
#         age = int(input("Enter your age: "))
#         address = input("Enter your address: ")
#         email = input("Enter your email: ")
#         return name, age, address, email

#     def get_user_input(self):
#         selected_bike = self.select_bike()
#         if selected_bike:
#             user_details = self.get_user_details()
#             return selected_bike, *user_details
#         return None
from colorama import Fore
from bikes_and_banks import RoyalEnfieldShowroom
from loan_process import LoanProcess

class UserInput:
    def get_user_input(self):
        showroom = RoyalEnfieldShowroom()
        loan_processor = LoanProcess()
        print(f"{Fore.GREEN}{'-'*20}Welcome to Royal Enfield Showroom!{'-'*20}{Fore.RESET}")
        want_bike = input("\n\nDo you want to buy a bike? (yes/no): ")
        if want_bike.lower() != 'yes':
            print("Thanks for visiting!")
            return
        else:
            print("Choose a bike:")
            for key, value in showroom.bikes.items():
                print(f"{Fore.RED}{key}{Fore.RESET}: {value[0]} - Price: {value[1]}")

            bike_choice = int(input(f"{Fore.BLUE}Enter the number corresponding to the bike you want: {Fore.RESET}"))
            selected_bike = showroom.bikes.get(bike_choice)
            if not selected_bike:
                print("Invalid choice!")
                return

            print(f"{Fore.CYAN}Please fill this form to confirm the order of your {selected_bike[0]}:{Fore.RESET}")
            name = input("Name: ")
            age = int(input("Age: "))
            if age < 18:
                print("Underage to buy a bike")
                return

            address = input("Address: ")
            email = input("Email Address: ")
            if '@' not in email:
                  print("Invalid email.")
                  return
            else:
             financial_proof = input("Financial Proof (e.g., bank statement, salary slip): ")

             bike_price = selected_bike[1]
             want_loan = input("Do you want a loan? (yes/no): ")

            # Pass the collected user information and bike details to the loan processor
             loan_processor.process_loan(bike_price, selected_bike, name, age, address, email, financial_proof, want_loan)
