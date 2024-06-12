#Write a Python program to create a person class. Include attributes like name,country and date of birth. Implement a method to determine the person's age.


from datetime import date

class Person:
    def __init__(self, name, country, year, month, date_birth):
        self.name = name
        self.country = country
        self.year = year
        self.month = month
        self.date_birth = date_birth

    def calculate_age(self):
        birthdate = date(self.year, self.month, self.date_birth)
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


name = input("Enter your name: ")
country = input("Enter your country: ")
year = int(input("Enter your year of birth: "))
month = int(input("Enter your month of birth (Enter as an integer, e.g., 'jan'='1'): "))
date_birth = int(input("Enter your date of birth: "))


person = Person(name, country, year, month, date_birth)


age = person.calculate_age()
print(person.name, "is", age, "years old.")
