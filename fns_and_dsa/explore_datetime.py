"""A module for calculating date and time"""
from datetime import datetime, timedelta

def display_current_datetime():
    """A function for checking the current date and time"""
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y - %m - %d %H : %M :%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    """Function for calculating a specified date"""
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(formatted_future_date)

def main():
    """
    Main function to run the datetime exploration script.
    """
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    calculate_future_date()

if __name__ == "__main__":
    main()
