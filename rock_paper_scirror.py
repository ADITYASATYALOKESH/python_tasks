import random

def machine():
    while True:  # Keep generating random choices
        yield random.choice(['rock', 'paper', 'scissors'])

# Create the generator
bot = machine()

# Play game
while True:
    user = input("Enter rock/paper/scissors or 'q' to quit: ").lower()
    if user == 'q':
        print("Game ended.")
        break
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid input, try again.")
        continue

    comp = next(bot)  # Get next machine move
    print(f"Machine chose: {comp}")

    # Decide winner
    if user == comp:
        print("It's a tie!\n")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print("You win!\n")
    else:
        print("Machine wins!\n")
