from player import Player
from game import Game

if __name__ == "__main__":
    player1_name = input("Enter name for Player 1: ")
    player1 = Player(player1_name)
    
    player2 = Player("Enemy")
    
    game = Game(player1, player2)

    while player1.score < 3 and player2.score < 3:
        game.play_round()

    if player1.score == 3:
        print(f"{player1.name} wins the game! {player2.name} is a loser!")
    else:
        print(f"{player2.name} wins the game! {player1.name} is a loser!")
