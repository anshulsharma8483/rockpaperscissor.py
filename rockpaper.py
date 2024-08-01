import random

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the choices
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Enter your choice: rock, paper, or scissors")
    
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Your choice: ").lower()
    
    # Validate user input
    while user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
    
    computer_choice = random.choice(choices)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
