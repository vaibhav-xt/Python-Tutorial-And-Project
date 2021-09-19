"""
f = open("Vaibhav.txt")
# print(f.tell())  # it tells that to find the position of file pointer
print(f.readline())  # to read one line
f.seek(100)   # this function is used to read line from the position you want.
print(f.readline())
f.close()
"""
 # Using With Block To Open Python files

with open("Vaibhav.txt") as f:
    a = f.readlines()
    print(a)

f = open("Vaibhav.txt", "rt")
print(f.readline())