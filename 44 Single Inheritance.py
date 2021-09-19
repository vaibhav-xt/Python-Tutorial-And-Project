# Single Inheritance

class Employee:
    no_of_leaves = 8
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
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return 34

# Single Inheritance
class programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. salary is {self.salary} and role is {self.role}. The languages " \
               f"are{self.languages}"

# Multi Inheritance
class player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class coolprogramer(Employee, player):
    language = "c++"
    def printlanguage(self):
        print(self.language)

rohan = player("Rohan", ["cricket"])
sks = coolprogramer("Karan", 343, "CoolProgrammer")
print(sks.printlanguage())

# harry = Employee("Harry", 435, "Instructor")
# karan = Employee.from_str("Karan-34-Students")
# subham = programmer("Rohan", 455, "Student", ["python", "cpp"])
# print(subham.printprog())
#
# print(karan.salary)
#
# harry.change_leaves(343)
# print(harry.no_of_leaves)
#
# print(harry.printgood("Harry"))
#


