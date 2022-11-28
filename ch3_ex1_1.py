# number guessing game
win_num = 60
user_input = int(input("Guess the number:-"))
if win_num == user_input:
    print("You win the game!!")
else:
    if user_input > win_num:
        print("Number is too high")
    else:
        print("Number is too low")
        
# Watch - COCO
name = input("Enter your name:-")
age = int(input("Enter your age:-"))
a = name[0]
if a == "a" or a =="A" and age > 10:
    print("You can watch COCO")
else:
    print("Sorry, You can't watch COCO")