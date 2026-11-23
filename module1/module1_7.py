def display_string(value):
    try:
        # Accept only string values.
        if not isinstance(value, str):
            raise TypeError("The value must be a string.")

        # Display the string.
        print(value)

    except TypeError:
        # Return None if the value is not a string.
        return None


# Test with a string.
display_string("Hello")

# Test with a non-string value.
result = display_string(25)
print("Result:", result)
