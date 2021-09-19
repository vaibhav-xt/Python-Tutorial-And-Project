"""
public = like youtube videos
protected = means information with your families only
private = like you private videos on youtube
"""

class Employee:
    no_of_leaves = 8
    var = 3   # here var and no_of_leaves are public

    # for protected - always started with '-'
    _protected = 7

    # for private - you have to use double underscore i.e. "__"
    __private = 34   # we cant print it directly like name.__private through an error
                     # but when we write name.Employee__private

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return 34

emp = Employee("Harry", 343, "Programmer")
print(emp._protected)
print(emp._Employee__private)

