def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

function_name_print("Harry", "Rohan", "SKillf", "Hammad", "shivam")
# but the above method is suitable for large data
# now for so much data

"""args :- allows the function to accept multiple arguments without knowing how any arguments.
           syntax : *args  and it can be written as you choice, but must start with * in the same way for kwargs"""

""" order :- normal, *args, **kwargs"""

def funargs(hat, *args, **kwargs):  # must remember noraml written first
    print(hat)
    print(type(args))   # args always in tuple not list when we pass list it converts into tuple
    print(args[4])  # in this method we have to give the position

# second method
    for i in args:
        print(i)
    print("Now I would Like to Introduce our heroes:")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
hat = "I am a normal Arguments and the students are:"
har = ["Harry", "Rohan", "SKillf", "Hammad", "shivam", "The programmer"]
ke = {"Rohan": "monitor", "harry": "coordinator"}
funargs(hat, *har, **ke)