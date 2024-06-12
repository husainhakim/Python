# from colorama import Fore
# from bikes_and_banks import RoyalEnfieldShowroom

# class LoanProcess:
#     def process_loan(self, bike_price, selected_bike, name, age, address, email, financial_proof, want_loan):
#         showroom = RoyalEnfieldShowroom()
#         payment_mode = ""
#         payment_amount_cash = 0
#         payment_amount_loan = 0
        
#         if want_loan.lower() == 'yes':
#             print("Choose a bank for a loan:")
#             for bank, interest_rate in showroom.banks.items():
#                 print(f"{bank} - Interest Rate: {interest_rate}%")

#             loan_bank = input("Enter the bank name for a loan: ").upper()
#             interest_rate = showroom.banks.get(loan_bank)
#             if not interest_rate:
#                 print("Invalid bank choice!")
#                 return None

#             loan_amount = int(input("Enter the loan amount: "))
#             if loan_amount >= bike_price:
#                 print("Loan amount should be less than the bike price.")
#                 return None

#             total_loan_amount = loan_amount + (loan_amount * (interest_rate / 100))
#             payment_amount_cash = bike_price - total_loan_amount
#             payment_amount_loan = total_loan_amount

#             print("Loan approved by the bank!")
#             payment_mode = f"Loan (Bank: {loan_bank}, Amount: {total_loan_amount})"
#         else:
#             payment_mode = "Cash"
#             payment_amount_cash = int(input("Enter the amount paid (in cash): "))
#             if payment_amount_cash < bike_price:
#                 remaining_amount = bike_price - payment_amount_cash
#                 print(f"The amount paid is less than the bike price. Please pay the remaining {remaining_amount} amount.")
#                 return None

#         return {
#             "payment_amount_cash": payment_amount_cash,
#             "payment_amount_loan": payment_amount_loan,
#             "payment_mode": payment_mode
#         }

# from colorama import Fore
# from bikes_and_banks import RoyalEnfieldShowroom

# class LoanProcess:
#     def process_loan(self, bike_price, selected_bike, name, age, address, email, financial_proof, want_loan):
#         showroom = RoyalEnfieldShowroom()
#         payment_mode = ""
#         payment_amount_cash = 0
#         payment_amount_loan = 0
        
#         if want_loan.lower() == 'yes':
#             print("Choose a bank for a loan:")
#             for bank, interest_rate in showroom.banks.items():
#                 print(f"{bank} - Interest Rate: {interest_rate}%")

#             loan_bank = input("Enter the bank name for a loan: ").upper()
#             interest_rate = showroom.banks.get(loan_bank)
#             if not interest_rate:
#                 print("Invalid bank choice!")
#                 return None

#             loan_amount = int(input("Enter the loan amount: "))
#             if loan_amount >= bike_price:
#                 print("Loan amount should be less than the bike price.")
#                 return None

#             total_loan_amount = loan_amount + (loan_amount * (interest_rate / 100))
#             payment_amount_cash = bike_price - total_loan_amount
#             payment_amount_loan = total_loan_amount

#             print("Loan approved by the bank!")
#             payment_mode = f"Loan (Bank: {loan_bank}, Amount: {total_loan_amount})"
#         else:
#             payment_mode = "Cash"
#             payment_amount_cash = int(input("Enter the amount paid (in cash): "))
#             remaining_amount = bike_price - payment_amount_cash
#             if payment_amount_cash < bike_price:
#                 print(f"The amount paid is less than the bike price. Please pay the remaining {remaining_amount} amount.")
#                 return None

#         return {
#             "payment_amount_cash": payment_amount_cash,
#             "payment_amount_loan": payment_amount_loan,
#             "payment_mode": payment_mode
#         }
# class BikeLoan:
#     def __init__(self, principal, rate, time):
#         self.principal = principal
#         self.rate = rate
#         self.time = time

#     def calculate_emi(self):
#         rate_per_month = self.rate / (12 * 100)
#         emi = (self.principal * rate_per_month * (1 + rate_per_month) ** self.time) / (
#                 (1 + rate_per_month) ** self.time - 1)
#         return emi

# def get_loan_details(): 
#     principal = float(input("Enter the loan amount: "))
#     time = int(input("Enter the loan duration in months: "))
#     return principal, time

# def main():
#     print("Welcome to the Bike Loan Calculator!")

#     banks = {
#         "SBI": 8.5, 
#         "ICICI BANK": 9.0,
#         "YES BANK": 9.5
#     }

#     print("Available Banks:\n")
#     for bank in banks:
#         print(bank)

#     selected_bank = input("Enter the name of the bank: ")
#     if selected_bank not in banks:
#         print("Invalid bank selection. Exiting.")
#         return

#     rate = banks[selected_bank]
#     principal, time = get_loan_details()
#     bike_loan = BikeLoan(principal, rate, time)
#     emi = bike_loan.calculate_emi()

#     print("\nLoan Details:")
#     print(f"Bank: {selected_bank}")
#     print(f"Loan Amount: {principal}")
#     print(f"Loan Duration: {time} months")
#     print(f"Interest Rate: {rate}%")
#     print(f"Monthly EMI: {emi:.2f}")

# if __name__ == "__main__":
#     main()
# class BikeLoan:
#     def __init__(self, principal, rate, time):
#         self.principal = principal
#         self.rate = rate
#         self.time = time

#     def calculate_emi(self):
#         rate_per_month = self.rate / (12 * 100)
#         emi = (self.principal * rate_per_month * (1 + rate_per_month) ** self.time) / (
#                 (1 + rate_per_month) ** self.time - 1)
#         return emi

# def get_loan_details(): 
#     principal = float(input("Enter the loan amount: "))
#     time = int(input("Enter the loan duration in months: "))
#     return principal, time

# def main():
#     print("Welcome to the Bike Loan Calculator!")

#     banks = {
#         "SBI": 8.5, 
#         "ICICI BANK": 9.0,
#         "YES BANK": 9.5
#     }

#     print("Available Banks:\n")
#     for bank in banks:
#         print(bank)

#     selected_bank = input("Enter the name of the bank: ")
#     if selected_bank not in banks:
#         print("Invalid bank selection. Exiting.")
#         return

#     rate = banks[selected_bank]
#     principal, time = get_loan_details()
#     bike_loan = BikeLoan(principal, rate, time)
#     emi = bike_loan.calculate_emi()

#     print("\nLoan Details:")
#     print(f"Bank: {selected_bank}")
#     print(f"Loan Amount: {principal}")
#     print(f"Loan Duration: {time} months")
#     print(f"Interest Rate: {rate}%")
#     print(f"Monthly EMI: {emi:.2f}")

# if __name__ == "__main__":
#     main()
from colorama import Fore
from bikes_and_banks import RoyalEnfieldShowroom
import time
class LoanProcess:
    def process_loan(self, bike_price, selected_bike, name, age, address, email, financial_proof, want_loan):
        showroom = RoyalEnfieldShowroom()
        payment_mode = ""
        payment_amount_cash = 0
        payment_amount_loan = 0
        if want_loan.lower() == 'yes':
            print("Choose a bank for a loan:")
            for bank, interest_rate in showroom.banks.items():
                print(f"{Fore.BLUE}{bank}{Fore.RESET} - Interest Rate: {Fore.GREEN}{interest_rate}%{Fore.RESET}")

            loan_bank = input("Enter the bank name for a loan: ").upper()
            interest_rate = showroom.banks.get(loan_bank)
            if not interest_rate:
                print("Invalid bank choice!")
                return

            loan_amount = int(input("Enter the loan amount: "))
            if loan_amount >= bike_price:
                print("Loan amount should be less than the bike price.")
                return

            total_loan_amount = loan_amount + (loan_amount * (interest_rate / 100))
            payment_amount_cash = bike_price - total_loan_amount
            payment_amount_loan = total_loan_amount

            print("Loan approved by the bank!")
            payment_mode = f"Loan (Bank: {loan_bank}, Amount: {total_loan_amount})"
        else:
            payment_amount_cash=bike_price
            total_loan_amount = 0
            payment_mode = "Cash"
            
        
        print("Generating a bill please standby.....")
        time.sleep(5)
        print(Fore.GREEN + "Receipt:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Address: {address}")
        print(f"Email: {email}")
        print(f"Cash Payment: {payment_amount_cash}")
        print(f"Loan Payment: {payment_amount_loan}")
        print(f"Payment Mode: {payment_mode}")
        print(f"Bike: {selected_bike[0]}")
        print(f"Price: {bike_price}")
        print("Thank you for your purchase!" + Fore.RESET)
