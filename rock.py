import random

while True:
    user_actions = input("Enter a choice (ROCK, PAPER, SCISSORS): ")
    possible_actions = ["ROCK", "PAPER", "SCISSORS"]
    computer_actions = random.choice(possible_actions)
    print(f"\nYou chose {user_actions}, computer chose {computer_actions}.\n")

    if user_actions == computer_actions:
        print(f"Both players selected {user_actions}. It's a tie!")
    elif user_actions == "ROCK":
        if computer_actions == "SCISSORS":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_actions == "PAPER":
        if computer_actions == "ROCK":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_actions == "SCISSORS":
        if computer_actions == "PAPER":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (yes/no): ")
    
    if play_again.lower() != "yes":
        
        break
