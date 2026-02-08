import random 

player = 0
computer = 0

my_list = ["scissors", "paper", "rock"]

while True:
    x = input("Choose rock paper or scissors: ").lower()

    if x == "quit":
        print("thank you for playing")
        print(f" The final score is {player} to {computer}")
        if player > computer:
            print("player wins")
        elif computer > player:
            print("computer wins")
        else:
            print("It is a tie")
        break
    


    if x in my_list:
        print(f"you have chose {x}")
        computer_choice = random.choice(my_list)
        print(f"computer has chose {computer_choice}")
    

        if x == computer_choice:
            print("It is a tie")
        elif x == "scissors" and computer_choice == "paper":
            print("you win scissors beats paper")
            player += 1
        elif x == "rock" and computer_choice == "scissors":
            print("you win rock beats scissors")
            player += 1
        elif x == "paper" and computer_choice == "rock":
            print("you win paper beats rock")
            player += 1
        else:
            print("computer wins")
            computer += 1

        print(f"The score is {player} to {computer}")
    else:
        print("choice is invalid")




