"""
f = open("story.txt", "rt")
# print(f.readline())
print(f.readlines())   # it return in list

# content = f.read()
# print(content)

# to read line by line

# for line in content:
# for line in f:
#    print(line, end="")
"""
"""
content = f.read(3097)
print("1", content)
content = f.read(987908)
print("2", content)
f.close()
"""
# WRITE

# h = open("story.txt", "w")
h = open("story.txt", "a")  # if we write a then file will open in append mode
a = h.write("Vaibhav bhai bahut acche hai\n")
print(a)    # it return no. of character
h.close()

h = open("story.txt", "r+")  # r+ means read and write both
print(h.read())
h.write("thankyou")