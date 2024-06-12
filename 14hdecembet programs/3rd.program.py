# #largest among three
# def sparshva(num1, num2, num3):
#     return max(num1, num2, num3)
# num1=int(input("Enter number 1:-"))
# num2=int(input("Enter number 2:-"))
# num3=int(input("Enter number 3:-"))
# result = sparshva(num1, num2,num3)
# print(f"{result} is the largest number among three")  
# #function for sum of a list
# def sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# sparshva = [1, 2, 3, 4, 5]
# result = sum(sparshva)
# print(result)  
# #functiom for multiples in a list
# def multiple(numbers):
#     total = 1
#     for num in numbers:
#         total *= num
#     return total
# sparshva = [59, 12, 13, 54, 75]
# result = multiple(sparshva)
# print(result)  
# # ⁠Write a python function to reverse a string
# def reverse(str1, len):
#     reverse=""
#     for i in range(len-1,-1,-1):
#         reverse+=str1[i]
#     print(reverse)

# teststring=str(input("Enter a string: "))
# reverse(teststring, len(teststring))
# #Write a python function to calculate factorial of a number (non-negative integer)
# def factorial(n):
#     if n < 0:
#         return "Positive integer daalo"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(2, n + 1):
#             fact *= i
#         return fact
# sparshva=int((input("Enter a positive integer:-")))
# result=factorial(sparshva)
# print(f"Factorial of{sparshva} is:-",result)
# # ⁠Write a python function to find square and cube of a number
# def sparshva(num):
#     square = num ** 2
#     cube = num ** 3
#     return square, cube
# hellosparshva=int(input("Enter the number you want the square and cube of:-"))
# result = sparshva(hellosparshva)
# print("Square:", result[0])
# print("Cube:", result[1])
# Write a python function to check weather a number is perfect or not
# def sparshva(num):
#     if num <= 0:
#         return False
    
#     hellosparshva = 0
#     for i in range(1, num):
#         if num % i == 0:
#             hellosparshva += i
    
#     return hellosparshva == num
# hisparshva=int(input("Enter a number sparshva:-"))
# result = sparshva(hisparshva)
# print(result)  

#Write a python function that accepts a string and counts the number of upper and lower case letters
# def sparshva(string):
#     upper = 0
#     lower = 0

#     for char in string:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1

#     return upper, lower
# hisparshva=input("Enter a string:-")
# result = sparshva(hisparshva)
# print("Uppercase count:-", result[0])
# print("Lowercase count:-", result[1])



# Write a python function that checks weather a passed string is a palindrome or not
# def reverse(input_string):
#     a=input_string[::-1]
#     if a==input_string:
#         print("palindrome")
#     else:
#         print("not palindrome")
# sparshva =input("Enter a string:-")
# reverse(sparshva)
