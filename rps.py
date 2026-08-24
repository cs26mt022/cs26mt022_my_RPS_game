import random


def main():
    print("Welcome to Rock Paper Scissors!")

    print("\nRules:")
    print("Rock beats scissors.")
    print("Scissors beats paper.")
    print("Paper beats rock.")
    print("If both players choose the same option, it is a tie.")

    player_choice = input("\nEnter your choice (rock, paper, or scissors): ")

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()