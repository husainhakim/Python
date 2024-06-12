# num = int(input("Enter a number to find its factorial: "))

# if num < 0:
#     print("Factorial cannot be found for negative numbers.")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")


# def count_upper_lower(text):
#     upper_count = 0
#     lower_count = 0

#     for char in text:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1

#     return upper_count, lower_count

# # Example usage:
# input_string = input("Enter a string: ")
# upper, lower = count_upper_lower(input_string)
# print(f"Number of uppercase letters: {upper}")
# print(f"Number of lowercase letters: {lower}")



# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# # Print Complete list
# print("Complete List:", a)

# # Print 4th element of list
# print("4th Element:", a[3])

# # Print list from 0th to 4th index
# print("0th to 4th Index:", a[0:5])

# # Print list -7th to 3rd element
# print("-7th to 3rd Element:", a[-7:4])

# # Appending an element to list
# a.append(110)
# print("List after Appending:", a)

# # Sorting the elements of list
# a.sort()
# print("Sorted List:", a)

# # Popping an element
# popped_element = a.pop()
# print("Popped Element:", popped_element)
# print("List after Popping:", a)



# # Define the list of countries in BRICS
# brics_countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']

# # Display the list of BRICS countries
# print("Countries in BRICS:")
# for country in brics_countries:
#     print(country)
# Define two dictionaries
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 1, 'b': 2, 'c': 3}

# # Compare dictionaries using the == operator
# if dict1 == dict2:
#     print("The dictionaries are equal.")
# else:
#     print("The dictionaries are not equal.")



# def add_matrices(matrix1, matrix2):
#     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
#         return "Matrices should have the same dimensions for addition."

#     result = []
#     for i in range(len(matrix1)):
#         row = []
#         for j in range(len(matrix1[0])):
#             row.append(matrix1[i][j] + matrix2[i][j])
#         result.append(row)

#     return result

# # Example matrices
# matrix_A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix_B = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# # Adding matrices
# result_matrix = add_matrices(matrix_A, matrix_B)

# # Displaying the result
# if isinstance(result_matrix, str):
#     print(result_matrix)
# else:
#     print("Resultant Matrix after Addition:")
#     for row in result_matrix:
#         print(row)
 
 
 
 
# original_list = [1, 2, 3, 4, 5]

# # Method 1: Using reverse() method
# reversed_list = original_list.copy()  # Create a copy to preserve the original list
# reversed_list.reverse()

# print("Traversing list in reverse order using reverse() method:")
# for item in reversed_list:
#     print(item)

# # Method 2: Using slicing
# reversed_list_slicing = original_list[::-1]

# print("\nTraversing list in reverse order using slicing:")
# for item in reversed_list_slicing:
#     print(item)


# hi=input("Enter your email:")
# User=print('Name:-husain')
# Domain=print('Domain:-gmail.com')


# class Grandfather:
#     def __init__(self):
#         self.gfname = " John  "
#         self.sername = " wick"
#         self.gfinherita = 5000
#         self.gfperchased = 5000
#         self.gfasset = self.gfinherita + self.gfperchased


# class Father(Grandfather):
#     def __init__(self):
#         super(Father, self).__init__()
#         self.fname = " rabinder " + self.gfname + self.sername
#         self.finherita = 500
#         self.fperchased = 500
#         self.fasset = self.finherita + self.fperchased


# class Husband:
#     def __init__(self):
#         self.hname = " Rita"
#         self.hsername = " Gaikwad"
#         self.hinherita = 50000
#         self.hperchased = 50000
#         self.hasset = self.hinherita + self.hperchased


# class Child(Father, Husband):
#     def __init__(self):
#         Father.__init__(self)
#         Husband.__init__(self)
#         self.cname = input("Enter your name : ")
#         self.cname += self.hname + self.hsername + self.fname
#         self.cinherita = self.finherita + self.gfinherita + self.hinherita
#         self.cperchased = self.fperchased + self.gfperchased + self.hperchased
#         self.casset = self.gfasset + self.fasset + self.hasset

#     def getdata(self):
#         print(f"\n\nHI, {self.cname}")
#         print(f"YOUR TOTAL ASSET: {self.casset}")
#         print(f"INHERITED: {self.cinherita}")
#         print(f"PURCHASED: {self.cperchased}")


# obj = Child()
# obj.getdata()



class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}\nEmployee Name: {self.emp_name}\nEmployee Salary: {self.emp_salary}"

    def print_employee_details(self):
        print(self.get_employee_details())


employee1 = Employee(emp_id=101, emp_name="John Doe", emp_salary=50000)


details = employee1.get_employee_details()
print("Employee Details (using get_employee_details method):\n", details)

print("\nEmployee Details (using print_employee_details method):")
employee1.print_employee_details()
