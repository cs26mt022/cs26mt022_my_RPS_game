import random


def main():
    print("Welcome to Rock Paper Scissors!")

    print("\nRules:")
    print("Rock beats scissors.")
    print("Scissors beats paper.")
    print("Paper beats rock.")
    print("If both players choose the same option, it is a tie.")

    choices = ["rock", "paper", "scissors"]
    round_number = 1

    while True:
        print(f"\nRound {round_number}")

        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        computer_choice = random.choice(choices)

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie! Rematch!")
            round_number += 1
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "scissors" and computer_choice == "paper")
            or (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
            break
        else:
            print("Computer wins!")
            break


if __name__ == "__main__":
    main()