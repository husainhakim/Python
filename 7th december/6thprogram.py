number = int(input("Enter the number of students: "))
topperkaname=""
topperkamarks=[]
for i in range (number):
    name=input(f"Enter the name of student{i+1}:")
    for i in range (4):
        marks=int(input(f"Enter the marks in {i+1} subject "))
        totalmarks=sum(marks)
        if totalmarks >sum(topperkamarks):
            topperkaname=name
            topperkamarks=marks
print(f"{name} is the topper with marks {topperkamarks} in the 4 subjects")
  