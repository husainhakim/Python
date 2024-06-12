# def fact(num):

#     if(num < 0):
#         return "Not negative number"
    
#     if(num<2):
#         return 1
    
#     else:
#         factorial = num * fact(num-1)
#         return factorial

# n = 1.2

# while(not(int(n) == n)):
#     try:
#         n = int(input("Enter the num : "))
#     except:
#         print("We take input as integer only")

    



# print(fact(n))

# def fact(num):
#     if num < 0:
#         return "Factorial is not defined for negative numbers"
#     elif num < 2:
#         return 1
#     else:
#         factorial = 1
#         for i in range(1, num + 1):
#             factorial *= i
#         return factorial

# while True:
#     try:
#         n = int(input("Enter an integer: "))
#         if n < 0:
#             print("Factorial is not defined for negative numbers.")
#         else:
#             print(f"Factorial of {n} is {fact(n)}")
#         break
#     except :
#         print("Invalid input. Please enter a non-negative integer.")

# while True:
#     hi = input("Enter a character: ")
#     try:
#         if len(hi) == 1:
#             ascii_value = ord(hi)
#             print(f'ASCII value of {hi} is {ascii_value}')
#             break  # Exit the loop if a single character is entered
#         else:
#             raise ValueError("Please enter only a single character.")
#     except ValueError as sparshva:
#         print(sparshva)
while True:
    try:
      hi =input("Enter a character: ")
      if len(hi)==(1):
          print(f"Length of {hi} is 1")
          break
      else:
          raise ValueError(f"Invalid input. Length of {hi} is {len(hi)} ,length can only be 1")
    except ValueError as sparshva:
        print(sparshva)
        