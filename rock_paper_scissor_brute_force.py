import random

def get_user_choice():
    choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please choose Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

def main():
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        result = play_game()
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Your score: {user_score}  Computer's score: {computer_score}")

    if user_score == 3:
        print("Congratulations! You win the game!")
    else:
        print("Computer wins the game. Better luck next time!")

if __name__ == "__main__":
    main()
