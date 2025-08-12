from datetime import datetime

def display_current_datetime():

    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%s")

    print(f"Current date and time: {formatted_date}")

    from datetime import datetime, timedelta

    def display_current_datetime():
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current date and time: {formatted_date}")

    def calculate_future_date():

        current_date = datetime.now()

        while True:
            try:
                days_to_add_str = input("Enter the number of days to add to the current date: ")
                days_to_add = int(days_to_add_str)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future_date}")

from datetime import datetime, timedelta 

def display_current_datetime(): 

    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    current_date = datetime.now()

    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()