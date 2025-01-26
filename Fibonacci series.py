def display_menu():
    print("\n--- Fibonacci Sequence Generator ---")
    print("1. Generate Fibonacci sequence (Iterative)")
    print("2. Generate Fibonacci sequence (Recursive)")
    print("3. Instructions")
    print("4. Exit")
    print("------------------------------------")


def generate_fibonacci_iterative(n):
    """Generates the Fibonacci sequence iteratively and stores it in a list."""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def generate_fibonacci_recursive(n, sequence=None):
    """Generates the Fibonacci sequence recursively."""
    if sequence is None:
        sequence = []
    if n <= 0:
        return sequence
    if len(sequence) < 2:
        sequence.append(len(sequence))  # Start with [0, 1]
    else:
        sequence.append(sequence[-1] + sequence[-2])
    return generate_fibonacci_recursive(n - 1, sequence)


def show_instructions():
    """Displays instructions for using the program."""
    print("\nInstructions:")
    print("1. Select option 1 for iterative Fibonacci sequence generation.")
    print("2. Select option 2 for recursive Fibonacci sequence generation.")
    print("3. Enter the number of terms (positive integer) when prompted.")
    print("4. You can save the generated sequence to a file.")
    print("5. Select option 4 or type 'close' to exit the program.")
    print("6. Invalid inputs will show error messages for guidance.")


def save_sequence_to_file(sequence, n, method):
    """Saves all inputs and generated Fibonacci sequences to a file."""
    filename = "fibonacci_sequences.txt"
    with open(filename, "a") as file:  # Open in append mode to save multiple entries
        file.write(f"Input: {n} terms | Method: {method} | Sequence: {sequence}\n")
    print(f"Sequence appended to '{filename}'.")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1" or choice == "2":
        method = "Iterative" if choice == "1" else "Recursive"
        generate_function = generate_fibonacci_iterative if choice == "1" else generate_fibonacci_recursive

        while True:
            user_input = input("Enter the number of terms in the Fibonacci series: ")
            if not user_input.isdigit() or int(user_input) <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                n = int(user_input)
                sequence = generate_function(n)
                print(f"Fibonacci sequence for {n} terms ({method}): {sequence}")

                # Options after generating sequence
                print("\nWhat would you like to do next?")
                print("1. Save the sequence to a file.")
                print("2. Try another number.")
                print("3. Close the program.")
                next_choice = input("Enter your choice (1/2/3): ")

                if next_choice == "1":
                    save_sequence_to_file(sequence, n, method)
                elif next_choice == "2":
                    continue  # Loop again to enter a new number
                elif next_choice == "3" or next_choice.lower() == "close":
                    print("Thank you for using the Fibonacci Sequence Generator. Goodbye!")
                    exit()
                else:
                    print("Invalid choice. Returning to number entry.")
                break

    elif choice == "3":
        show_instructions()

    elif choice == "4" or choice.lower() == "close":
        print("Thank you for using the Fibonacci Sequence Generator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
