class A:
    classVar1 = "I am in class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classVar1 = "Instance var in class A"
class B(A):
    classVar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classVar1 = "Instance var in class B"
        super().__init__()   # it will print class A self.classVar1
        print(super().classVar1)

# instance
a = A()
b = B()

print(b.classVar1)