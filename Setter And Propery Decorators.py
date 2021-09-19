class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@rexteria.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email Not Set"
        return f"{self.fname}.{self.lname}@rexteria.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]  # it return list
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.explain())
print(hindustani_supporter.email)

hindustani_supporter.fname = "US"
print(hindustani_supporter.email)

hindustani_supporter.email = "this.that@rexteria.com"
print(hindustani_supporter.fname, hindustani_supporter.lname, hindustani_supporter.email)

del hindustani_supporter.email
print(hindustani_supporter.email)
