import random

player_score = 0
computer_score = 0

print("Welcome to rock paper scissors game...!!!")
print("play with your computer and enjoy....!!!")
while True:
    player_choice = int(input("Select your choice: 0 for rock, 1 for paper, 2 for scissors: "))
    if player_choice >= 3 or player_choice < 0:
        print("You entered an invalid number.")
    else:
        computer_choice = random.randint(0, 2)
        print("Computer choice:", computer_choice)
        if computer_choice == player_choice:
            print("It's a draw")
        elif computer_choice == 0 and player_choice == 1:
            print("You Win")
            player_score += 1
        elif computer_choice == 0 and player_choice == 2:
            print("You Lost")
            computer_score += 1
        elif computer_choice == 1 and player_choice == 0:
            print("You win")
            player_score +=1
        elif computer_choice == 1 and player_choice == 2:
            print("You Lost")
            computer_score +=1
        elif computer_choice == 2 and player_choice == 0:
            print("you win")
            player_score +=1
        else:
            print("You lose")
            computer_score += 1
            
        print("Your Score:", player_score)
        print("Computer Score:", computer_score)
        
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("thank you for playing game..!!")
        print("As per your wish the game has end....")
        break