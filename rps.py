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


if __name__ == "__main__":
    main()