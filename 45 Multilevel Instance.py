# Multilevel Inheritance
"""
class Dad:
    basketball = 1

class son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no of times."

class grandson(son):
    dance = 6
    def isdance(self):
        return f"Jackson Yeah!" \
            f"Yes I dance {self.dance} no of times."

darry = Dad()
larry = son()
harry = grandson()

print(harry.isdance())
print(darry.basketball)
"""

