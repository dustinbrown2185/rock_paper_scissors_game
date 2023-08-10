class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        choice1 = self.player1.get_user_choice()
        choice2 = self.player2.get_computer_choice()

        print(f"{self.player1.name}: {choice1}")
        print(f"{self.player2.name}: {choice2}")

        if choice1 == choice2:
            print("It's a tie!")
        elif (choice1 == "rock" and choice2 == "scissors") or \
             (choice1 == "scissors" and choice2 == "paper") or \
             (choice1 == "paper" and choice2 == "rock"):
            print(f"{self.player1.name} wins!")
            self.player1.score += 1
        else:
            print(f"{self.player2.name} wins!")
            self.player2.score += 1
