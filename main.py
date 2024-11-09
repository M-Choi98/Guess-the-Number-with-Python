import random

# Task 1: Guess the number through user input
def guess_random_number(tries, start, stop):
    target_number = random.randint(start, stop)

    while tries > 0:
        print(f"Number of tries left: {tries}")
        try:
            guess = int(input(f"Guess a number between {start} and {stop}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess == target_number:
            print("Congratulations! You guessed the number!")
            return
        elif guess < target_number:
            print("Guess higher!")
        else:
            print("Guess lower!")
        tries -= 1
    # out of tries
    print(f"Sorry, you are out of tries. The correct number was {target_number}.")


# Task 2: Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)
    print(f"The number for the program to guess is: {target_number}")

    # Linear
    for guess in range(start, stop + 1):
        if tries == 0:
            print("Sorry, the program ran out of tries.")
            return
        print(f"The program is guessing....{guess}")
        if guess == target_number:
            print("The program guessed the correct number!")
            return
        tries -= 1
        print("The program failed to guess the correct number...")


# Task 3: Guess the number programmatically using binary search
def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)
    print(f"The number for the program to guess is: {target_number}")
    # search range
    low = start
    high = stop
    while tries > 0:
        # Binary search
        guess = (low + high) // 2
        print(f"The program is guessing....{guess}")
        if guess == target_number:
            print(f"Found it! {guess}")
            return
        elif guess < target_number:
            print("Guessing higher!")
            low = guess + 1
        else:
            print("Guessing lower!")
            high = guess - 1
        tries -= 1
    print("The program couldn't guess the number.")

# Task 1 Test
"""guess_random_number(5, 0, 10)"""
#Task 2 Test
"""guess_random_num_linear(5, 0, 10)"""
# Task 3 Test
guess_random_num_binary(5, 0, 100)
