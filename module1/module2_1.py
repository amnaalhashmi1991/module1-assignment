def check_even_or_odd(number):
    # Check the remainder after dividing by 2.
    if number % 2 == 0:
        return "Even"
    return "Odd"


# Test the function.
print(check_even_or_odd(8))
print(check_even_or_odd(5))
