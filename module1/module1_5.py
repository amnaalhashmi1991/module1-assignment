def shift_text_and_calculate_price(text, price_per_letter):
    # English alphabets used to shift letters.
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    shifted_text = ""
    letter_count = 0

    # Shift each English letter by one.
    for character in text:
        if character in lowercase:
            index = lowercase.index(character)
            shifted_text += lowercase[(index + 1) % 26]
            letter_count += 1
        elif character in uppercase:
            index = uppercase.index(character)
            shifted_text += uppercase[(index + 1) % 26]
            letter_count += 1
        else:
            # Keep spaces and punctuation unchanged.
            shifted_text += character

    # Count words and calculate the price of the letters.
    word_count = len(text.split())
    total_price = letter_count * price_per_letter

    # Return the results in a dictionary.
    return {
        "shifted_text": shifted_text,
        "word_count": word_count,
        "price": total_price
    }


# Test the function.
result = shift_text_and_calculate_price("Hello, world!", 2)
print(result)
