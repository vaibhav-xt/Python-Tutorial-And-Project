import os

print(dir(os))  # its shows all the method that we can do with OS module.
print(os.getcwd())
# os.chdir("C://")  # It will change the directory
print(os.listdir())  # it will show all the file present in directory also we can write the directory in the prenthesis.
# os.mkdir("this")   # it will make the folder in directory
# os.makedirs("this/that")  # it will make the folder of this and that
# os.rename("name of the folder", "new name of the folder")
print(os.path.join("C://", "/harry.txt"))
# print(os.path.exists("write the directory"))
