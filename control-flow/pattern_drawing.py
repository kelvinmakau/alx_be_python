# pattern_drawing.py

# Prompt the user for pattern size
try:
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Please enter a positive integer.")
    else:
        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1

except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
