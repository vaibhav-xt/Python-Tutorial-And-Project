
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}."

harry = Employee("Harry", 455, "Instructor")
# Harry = Employee()
# Rohan = Employee()
#
# Harry.name = "Harry"
# Harry.salary = 343
# Harry.role = "Instructor"
# Harry.no_of_leaves = 33
#
#
# Rohan.name = "Harry"
# Rohan.salary = 675
# Rohan.role = "Student"

# print(Rohan.printdetails())

# constructor
print(harry.salary)
print(harry.name)