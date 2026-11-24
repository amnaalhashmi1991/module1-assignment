def get_unique_numbers(numbers):
    unique_numbers = []

    # Add each number only once.
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


# Test the function.
numbers = [1, 2, 2, 3, 1, 4]
result = get_unique_numbers(numbers)

print("Original list:", numbers)
print("Unique numbers:", result)
