# Human Diet Program

from datetime import datetime

def lockdata():
    detail = input("Enter to lock(Food, Exercise): ")
    detail = detail.capitalize()
    if detail == "Food":
        food = input("Enter Food Name: ")
        food = food.capitalize()
        with open("food.txt", "a") as f:
            f.write(f"{food}: {datetime.now()}\n")
            print("Successfully Added!\n")
            print("--------------------------------------------------\n")
        f.close()

    elif detail == "Exercise":
        exer = input("Enter Exercise: ")
        exer = exer.capitalize()
        with open("exercise.txt", "a") as f:
            f.write(f"{exer}: {datetime.now()}")
            print("Successfully Added!\n")
            print("--------------------------------------------------\n")
        f.close()

    else:
        print("Enter(Food or Exercise)\n")
        lockdata()


def retrieve_date():
    detail = input("Enter(Food, Exercise) to Retrieve Date: ")
    detail = detail.capitalize()
    if detail == "Food":
        user_food = input("Enter User Name:")
        user_food = user_food.capitalize()
        with open("food.txt") as f:
            if user_food in f:
                line = f.read()
                print(line)
                print("--------------------------------------------------\n")
            else:
                print("Entered Details Are Not In Current Record!")
                print("--------------------------------------------------\n")
        f.close()

    elif detail == "Exercise":
        user_exercise = input("Enter Exercise Name: ")
        user_exercise = user_exercise.capitalize()
        with open("exercise.txt") as f:
            if user_exercise in f:
                line = f.read()
                print(line)
                print("--------------------------------------------------\n")
            else:
                print("Entered Details Not In Current Record!")
                print("--------------------------------------------------\n")
        f.close()
    else:
        print("Enter(Food or Exercise)\n")
        retrieve_date()

while True:
    print("--------------------------------------------------")
    print("  <<\ \Human Diet Program/ />>")
    print("1. Lock Data\n2. Retrieve Date\n3. Exit")
    print("--------------------------------------------------\n")
    choice = input("Enter You Choice: ")
    if int(choice) == 1:
        lockdata()
    elif int(choice) == 2:
        retrieve_date()
    elif int(choice) == 3:
        exit()

