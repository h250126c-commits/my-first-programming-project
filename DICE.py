import random  # Import the random module to generate random numbers

def throw_dice():

    # randint(a, b) returns a random integer N such that a <= N <= b
    return random.randint(1, 6)

# Main program
if __name__ == "__main__":
    print("🎲 Dice Thrower 🎲")

    # Ask the user if they want to throw the dice
    while True:
        user_input = input("Press Enter to throw the dice or type 'q' to quit: ").lower()

        if user_input == 'q':
            print("Goodbye!")
            break  # Exit the loop if the user wants to quit

        # Throw the dice and print the result
        dice_value = throw_dice()
        print(f"You threw a {dice_value}!\n")

