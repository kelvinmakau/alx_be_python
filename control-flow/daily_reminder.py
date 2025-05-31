# daily_reminder.py

# Prompt for a single task
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        message = f"High Priority: {task}."
    case "medium":
        message = f"Medium Priority: {task}."
    case "low":
        message = f"Low Priority: {task}."
    case _:
        message = f"Priority not recognized for task: {task}."

# Modify message if task is time-bound
if time_bound == "yes":
    message += " This is a time-sensitive task that requires immediate attention today!"

# Print the customized reminder
print("\nReminder:")
print(message)
