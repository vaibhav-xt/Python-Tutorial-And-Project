# Snake Water and Gun
import random
total_round = 10
current_round = 0
your_round = 0
cpu_round = 0
print("--------------------------------------------------------")
print("      *** ** * SNAKE WATER AND GUN * ** ***")
print("    Maximum 10 Rounds You Have To Win The Game")
print("--------------------------------------------------------\n")
while current_round < 10:
    user_input = input("Enter You Choice(Snake, Water And Gun):- ")
    user_input = user_input.capitalize()
    cpu_option = ["Snake", "Water", "Gun"]
    cpu_choice = random.choice(cpu_option)
    if user_input in cpu_option:

        print(f"CPU Choice: {cpu_choice}")

        if user_input == cpu_choice:
            print("Match Get Tie! No One Get The Point\n")

        elif cpu_choice == "Snake":
            if user_input == "Water":
                print("CPU Win!\n")
                cpu_round = cpu_round + 1
            elif user_input == "Gun":
                print("You Win\n")
                your_round = your_round + 1

        elif cpu_choice == "Water":
            if user_input == "Snake":
                print("You Win!\n")
                your_round = your_round + 1
            elif user_input == "Gun":
                print("CPU Win\n")
                cpu_round = cpu_round + 1

        elif cpu_choice == "Gun":
            if user_input == "Water":
                print("You Win!\n")
                your_round = your_round + 1
            elif user_input == "Snake":
                print("CPU win!\n")
                cpu_round = cpu_round + 1

        current_round = current_round + 1

    else:
        print("You Exceeds Your Limit. Try Again!\n")

if your_round > cpu_round:
    print(f"Congratulation You Win! \n{your_round} is your Score. CPU score {cpu_round} ")

elif cpu_round > your_round:
    print(f"You Lost Match!\n{your_round} is your Score. CPU score {cpu_round}")

elif cpu_round == your_round:
    print(f"Match Draw!\n{your_round} is your Score. CPU score {cpu_round}")

print("-------------------------------------------------------\n")