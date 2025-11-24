from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: Display the Current Date and Time
    """
    # Obtain the current date and time using datetime.now()
    # Instruction: save the current date inside a current_date variable
    current_date = datetime.now()
    
    # Instruction: Format and print in "YYYY-MM-DD HH:MM:SS" format
    # We use strftime (String Format Time) to achieve this layout
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Part 2: Calculate a Future Date
    """
    # Instruction: Prompt the user to enter a number of days
    try:
        days_to_add = int(input("Enter number of days to add to the current date: "))
        
        # Get the current date again to base the calculation on right now
        current_date = datetime.now()
        
        # Instruction: Calculate date after adding the days
        # We use timedelta to represent the duration of days
        time_change = timedelta(days=days_to_add)
        
        # Instruction: save the future date inside a future_date variable
        future_date = current_date + time_change
        
        # Instruction: Print the future date in "YYYY-MM-DD" format
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"The date {days_to_add} days from now will be: {formatted_future}")
        
    except ValueError:
        print("Error: Please enter a valid whole number.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()
    print("-" * 30) # Just a separator line for readability
    calculate_future_date()