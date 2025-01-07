import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game function
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    # Take the player's choice
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    # Get the computer's choice
    computer_choice = get_computer_choice()
    
    # Print both choices
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine and display the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Play the game
if __name__ == "__main__":
    play_game()
