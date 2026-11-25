import random

CHOICES = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# 2D table determining win (1), lose (-1), or tie (0)
# Rows = Computer Choice, Columns = Player Choice
PAYOFF_TABLE = [
    [ 0,  1, -1, -1,  1],  # Computer = Rock
    [-1,  0,  1,  1, -1],  # Computer = Paper
    [ 1, -1,  0, -1,  1],  # Computer = Scissors
    [ 1, -1,  1,  0, -1],  # Computer = Lizard
    [-1,  1, -1,  1,  0]   # Computer = Spock
]

wins = 0
ties = 0
losses = 0

while True:
    print("\n--- Rock-Paper-Scissors-Lizard-Spock ---")
    print("0: Rock | 1: Paper | 2: Scissors | 3: Lizard | 4: Spock")
    
    player_choice = int(input("Enter your choice (0-4): "))
    if player_choice not in [0, 1, 2, 3, 4]:
        print("Invalid entry! Choose an integer from 0 to 4.")
        continue

    computer_choice = random.randint(0, 4)

    print(f"Player Choice: {CHOICES[player_choice]}")
    print(f"Computer Choice: {CHOICES[computer_choice]}")

    outcome = PAYOFF_TABLE[computer_choice][player_choice]

    if outcome == 1:
        print("Round Outcome: You Win!")
        wins += 1
    elif outcome == -1:
        print("Round Outcome: You Lose!")
        losses += 1
    else:
        print("Round Outcome: It's a Tie!")
        ties += 1

    print(f"Total Stats -> Wins: {wins} | Ties: {ties} | Losses: {losses}")

    again = input("\nPlay another round? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing!")
        break