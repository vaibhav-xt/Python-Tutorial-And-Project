# Guess the Number, Got 9 chances to win.

print("*** ** * Welcome to Guess The Number Game * ** ***")
n = 18
guesses = 1
print("You have only 9 chances to win:-")
while guesses <= 9:
    i = int(input("Enter Value:"))
    if i < 18:
        print("Please Increase The number.")
        print("You Miss The Chance. Remaining Chance ", 9 - guesses)
    elif i > 18:
        print("Please Decrease The Number.")
        print("You Miss The Chance. Remaining Chance ", 9 - guesses)
    else:
        print("You Won The Game.")
        print(guesses, "no. of guesses he took to finish The Game.")
        break
    guesses = guesses + 1
if guesses > 9:
    print("Game Over!")
    print("You have lost all chances.")