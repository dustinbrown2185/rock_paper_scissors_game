import mysql.connector
from datetime import datetime
import atexit

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dust-Boy1'
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS rock_paper_scissors")

# Close the cursor and connection
cursor.close()
conn.close()

# Connect to the 'rock_paper_scissors' database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dust-Boy1',
    database='rock_paper_scissors'
)

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create the 'scores' table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                  (username VARCHAR(255), points INTEGER, date TIMESTAMP)''')

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
            print(f"{self.player1.name} score: {self.player1.score}\n{self.player2.name} score: {self.player2.score}\n")
        elif (choice1 == "rock" and choice2 == "scissors") or \
             (choice1 == "scissors" and choice2 == "paper") or \
             (choice1 == "paper" and choice2 == "rock"):
            print(f"{self.player1.name} wins!")
            self.player1.score += 1
            self.update_score(self.player1)
            print(f"{self.player1.name} score: {self.player1.score}\n{self.player2.name} score: {self.player2.score}\n")
        else:
            print(f"{self.player2.name} wins!")
            self.player2.score += 1
            self.update_score(self.player2)
            print(f"{self.player1.name} score: {self.player1.score}\n{self.player2.name} score: {self.player2.score}\n")

    def update_score(self, player):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_query = "INSERT INTO scores (username, points, date) VALUES (%s, %s, %s)"
        values = (player.name, player.score, date)
        cursor.execute(insert_query, values)
        conn.commit()
        print(f"\nInserted score for {player.name}: {player.score} at {date}")
    
    def display_results(self):
        if self.player1.score > self.player2.score:
            winner = self.player1.name
            loser = self.player2.name
        elif self.player2.score > self.player1.score:
            winner = self.player2.name
            loser = self.player1.name
        else:
            winner = "No one"
            loser = "No one"
        
        print(f"{winner} wins the game! {loser} is a loser!")

# Close the database connection when the program ends
atexit.register(conn.close)
