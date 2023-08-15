import random
import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('game_scores.db')
cursor = conn.cursor()

# Create the table to store user scores if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (username TEXT, points INTEGER, date TEXT)''')

class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0

class Enemy:
    def __init__(self, name):
        self.name = name
        self.choices = ['Rock', 'Paper', 'Scissors']
    
    def make_choice(self):
        return random.choice(self.choices)

def play_round(player, enemy):
    print(f"Round against {enemy.name}:")
    player_choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
    enemy_choice = enemy.make_choice()
    print(f"Enemy chose {enemy_choice}")
    
    if (player_choice == 'Rock' and enemy_choice == 'Scissors') or \
       (player_choice == 'Paper' and enemy_choice == 'Rock') or \
       (player_choice == 'Scissors' and enemy_choice == 'Paper'):
        player.score += 1
        print("You win!")
    elif player_choice == enemy_choice:
        print("It's a tie!")
    else:
        print("You lose!")
        return False
    return True

def main():
    username = input("Enter your username: ")
    player = Player(username)
    
    enemies = [Enemy('Enemy 1'), Enemy('Enemy 2'), Enemy('Enemy 3')]
    
    for enemy in enemies:
        print(f"\nWelcome, {player.username}! Get ready to battle {enemy.name}!\n")
        
        win_streak = 0
        for _ in range(3):  # Best out of 3
            if play_round(player, enemy):
                win_streak += 1
            else:
                break
        
        if win_streak == 3:
            print(f"\nCongratulations, {player.username}! You defeated {enemy.name} and earned 50 points!\n")
            player.score += 50
        elif win_streak == 2:
            print(f"\nYou won best out of 3 against {enemy.name} and earned 25 points!\n")
            player.score += 25
        else:
            print(f"\nSorry, {player.username}, you lost against {enemy.name}. Game over!")
            break
    
    print(f"\nTotal score for {player.username}: {player.score}")
    
    # Record user's score in the database
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO scores VALUES (?, ?, ?)", (player.username, player.score, date))
    conn.commit()
    
    # Display top 5 scores
    top_scores = cursor.execute("SELECT username, points, date FROM scores ORDER BY points DESC LIMIT 5")
    print("\nTop 5 Scores:")
    for row in top_scores:
        print(f"{row[0]} - {row[1]} points ({row[2]})")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
