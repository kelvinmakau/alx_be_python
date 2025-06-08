# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate and display a future date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)  # Add specified days
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Please enter a valid integer.")

# Main execution
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
