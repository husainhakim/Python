# class Parent:
#     def add(self, x, y):
#         return x + y

# class Child(Parent):
#     def takevalue(self):
#         x = int(input("Enter x:-"))  
#         y = int(input("Enter y:-"))
#         return self.add(x, y) 
# hi = Child()  
# result = hi.takevalue()  
# print(result)

# class Shape:
#     def area(self,x,y):
#         return x*y
# class Square(Shape):
#     def hello(self):
#         x=int(input("Enter x:- "))
#         y=int(input("Enter y:- "))
#         return self.area(x,y)
# hi=Square()
# result=hi.hello()
# print(result)




# class Parent():
#     def add (self,x,y):
#         print(self.x+self.y)
# class Child (Parent):
#     def takevalue(self):
#         self.x=int(input("Enter x:- "))
#         self.y=int(input("Enter y:- "))
#         Parent.add(self.x,self.y)
# c=Child()
# chikne=c.takevalue()
# print(c)



# class Shape:     

#     def calculationwalajagaah(self, shape,side,width):
#         if shape.lower()=="square":
#              area=side**2
#         elif shape.lower()=="rectangle":
#              area=side*width

# class Rectangleyafirsquare(Shape):
#     def area(self):
#         shape = input("Enter the shape (square/rectangle): ")

#         if shape.lower() == "square":
#             side = float(input("Enter the length of a side: "))
#             return self.calculationwalajagaah(shape, side,0)
#         elif shape.lower() == "rectangle":
#             length = float(input("Enter the length of the rectangle: "))
#             width = float(input("Enter the width of the rectangle: "))
#             return self.calculationwalajagaah(shape, length, width)
#         else:
#             return "Invalid input"
# hi=Rectangleyafirsquare()
# a=hi.area()
# print(a)




# class Shape:     
#     def calculationwalajagaah(self, shape, side, width):
#         if shape.lower() == "square":
#             area = side ** 2
#         elif shape.lower() == "rectangle":
#             area = side * width
#         return area  

# class Rectangleyafirsquare(Shape):
#     def area(self):
#         shape = input("Enter the shape (square/rectangle): ")

#         if shape.lower() == "square":
#             side = int(input("Enter the length of a side: "))
#             return self.calculationwalajagaah(shape, side, 0)
#         elif shape.lower() == "rectangle":
#             length = int(input("Enter the length of the rectangle: "))
#             width = int(input("Enter the width of the rectangle: "))
#             return self.calculationwalajagaah(shape, length, width)
#         else:
#             return "Invalid input"

# hi = Rectangleyafirsquare()
# a = hi.area()
# print(a)






# class Letsupgrade():
#          def teachers(self):
#              self.teachers={'Physics':{'Name':'Mr. king areeb','Duration':'3 months'},'Mathemtics':{'Name':'Mrs. queen areeb','Duration':'4 months'},'Chemistry':'Mr. karunesh chikne','Duration':'2 months'}
             


# class LetsUpgrade:
#     lu_courses=[{'Subject': 'Mathematics', 'Trainer': 'Sai sir', 'Duration': 100},
#                 {'Subject': 'Python', 'Trainer': 'Saikiran', 'Duration': 150},
#                 {'Subject': 'Web design', 'Trainer': 'Prasad', 'Duration': 130}]

# class ITM:
#     itm_courses=[{'Subject': 'Math', 'Trainer': 'Sheetal', 'Duration': 90},
#                 {'Subject': 'DSA', 'Trainer': 'Sumit', 'Duration': 200},
#                 {'Subject': 'Computer Fundamentals', 'Trainer': 'Sumit', 'Duration': 150}]

# class CourseSelector(LetsUpgrade, ITM):
#     def print_subjects(self, selected_class):
#         if selected_class == 'LetsUpgrade':
#             subjects = [course['Subject'] for course in self.lu_courses]
#         elif selected_class == 'ITM':
#             subjects = [course['Subject'] for course in self.itm_courses]
#         else:
#             subjects = []

#         if not subjects:
#             print(f"No subjects available for {selected_class}")
#             return

#         print(f"Available subjects for {selected_class}: {subjects}")

#         selected_subject = input("Enter the subject you want details for: ")

#         if selected_subject in subjects:
#             if selected_class == 'LetsUpgrade':
#                 selected_course = next(course for course in self.lu_courses if course['Subject'] == selected_subject)
#             elif selected_class == 'ITM':
#                 selected_course = next(course for course in self.itm_courses if course['Subject'] == selected_subject)

#             print(f"\nDetails of {selected_subject} in {selected_class}:")
#             print(f"Trainer: {selected_course['Trainer']}")
#             print(f"Duration: {selected_course['Duration']} hours")
#         else:
#             print(f"{selected_subject} is not available in {selected_class}")

# course_selector = CourseSelector()

# selected_class = input("Enter the class (LetsUpgrade or ITM): ")
# course_selector.print_subjects(selected_class)


# class LetsUpgrade:
#     lu_courses=[{'Subject': 'Mathematics', 'Trainer': 'Sai sir', 'Duration': 100},
#                 {'Subject': 'Python', 'Trainer': 'Saikiran', 'Duration': 150},
#                 {'Subject': 'Web design', 'Trainer': 'Prasad', 'Duration': 130}]

# class ITM:
#     itm_courses=[{'Subject': 'Math', 'Trainer': 'Sheetal', 'Duration': 90},
#                 {'Subject': 'DSA', 'Trainer': 'Sumit', 'Duration': 200},
#                 {'Subject': 'Computer Fundamentals', 'Trainer': 'Sumit', 'Duration': 150}]

# class CourseSelector(LetsUpgrade, ITM):
#     def print_subjects(self, selected_class):
#         if selected_class == 'LetsUpgrade':
#             subjects = [haggu['Subject'] for haggu in self.lu_courses]
#         elif selected_class == 'ITM':
#             subjects = [haggu['Subject'] for haggu in self.itm_courses]
#         else:
#             subjects = []

#         if not subjects:
#             print(f"No subjects available for {selected_class}")
#             return

#         print(f"Available subjects for {selected_class}: {subjects}")

#         selected_subject = input("Enter the subject you want details for: ")

#         if selected_subject in subjects:
#             if selected_class == 'LetsUpgrade':
#                 selected_course = next(course for course in self.lu_courses if course['Subject'] == selected_subject)
#             elif selected_class == 'ITM':
#                 selected_course = next(course for course in self.itm_courses if course['Subject'] == selected_subject)

#             print(f"\nDetails of {selected_subject} in {selected_class}:")
#             print(f"Trainer: {selected_course['Trainer']}")
#             print(f"Duration: {selected_course['Duration']} hours")
#         else:
#             print(f"{selected_subject} is not available in {selected_class}")

# course_selector = CourseSelector()

# selected_class = input("Enter the class (LetsUpgrade or ITM): ").upper()
# course_selector.print_subjects(selected_class)
class Grandparent:
    def __init__(self):
       
        self.paisa = 0
          
    def dada(self):
        # print("ROMILVA")
        self.paisa += 5000


class Parent(Grandparent):
    def __init__(self):
        super().__init__() 
        self.papa()
        self.dada()

    def papa(self):
        # print("SPARSHVA")
        self.paisa += 9421


class Child(Parent):
    def __init__(self):
        super().__init__()  
        self.bacha()
      
    def bacha(self):
        # print("KINGVA")
        self.paisa += 1000
class Husband(Child):
    def __init__(self):
        super().__init__()
        self.bacha()
        self.husband()
    def husband(self):
        # print("KARUNESH")
        self.paisa+=10000000
        

hi = Grandparent()

print("Daada ka paisa", hi.paisa)
hi2 = Parent()
print("Paapa ka paisa", hi2.paisa)
hi3 = Child()
print("Bache ka paisa", hi3.paisa)
hi4=Husband()
print("Wife ka husband paisa",hi4.paisa)
