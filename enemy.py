import random

class Enemy:
    def __init__(self, name):
        self.name = name

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])
