

class Employee:
    no_of_leaves = 8
    pass

Harry = Employee()
Rohan = Employee()

Harry.name = "Harry"
Harry.salary = 343
Harry.role = "Instructor"
Harry.no_of_leaves = 33


Rohan.name = "Harry"
Rohan.salary = 675
Rohan.role = "Student"

print(Harry.name)
print(Harry.no_of_leaves)
print(Employee.no_of_leaves)
Rohan.no_of_leaves = 21


print(Rohan.__dict__)
print(Harry.__dict__)
print(Employee.__dict__)

# notice that here no of leaves is different for harry, rohan and employee
