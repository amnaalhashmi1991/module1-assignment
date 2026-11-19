from datetime import datetime


def get_today_datetime():
    # Get the current date and time.
    now = datetime.now()

    # Format: seconds:minutes:hours, day/month/year
    return now.strftime("%S:%M:%H, %d/%m/%Y")


def get_fibonacci_sequence():
    # Use twice the current minute as the number of terms.
    number_of_terms = datetime.now().minute * 2

    sequence = []
    first_number = 0
    second_number = 1

    # Build the Fibonacci sequence.
    for _ in range(number_of_terms):
        sequence.append(first_number)
        first_number, second_number = second_number, first_number + second_number

    return sequence


# Test the functions.
print("Today's date and time:", get_today_datetime())
print("Fibonacci sequence:", get_fibonacci_sequence())
