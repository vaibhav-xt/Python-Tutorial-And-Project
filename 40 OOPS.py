# Object Oriented Program

# classes - are Templates (like form we fill only the details which is easy)
# object - instance of the class
# class work on DRY(Do Not repeat Yourself)

class student:
    pass

harry = student()
larry = student()

# instance
harry.name = "Harry"
harry.std = 12
harry.section = 1

print(harry, larry)
print(harry.std, larry)