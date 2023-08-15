import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_display_name(self):
        if self.name == "Enemy":
            return "Enemy"
        else:
            return self.name

    def get_user_choice(self):
        valid_choices = ["rock", "paper", "scissors"]
        choice = input(f"{self.name}, enter your choice (rock/paper/scissors): ")
        while choice.lower() not in valid_choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            choice = input(f"{self.name}, enter your choice (rock/paper/scissors): ")
        return choice.lower()

    @staticmethod
    def get_computer_choice():  # Use @staticmethod decorator
        return random.choice(["rock", "paper", "scissors"])
