def encrypt_text(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    # Check each character in the text.
    for character in text.lower():
        if character in alphabet:
            index = alphabet.index(character)
            next_index = (index + 1) % 26
            encrypted_text += alphabet[next_index]
        else:
            # Keep spaces and punctuation unchanged.
            encrypted_text += character

    return encrypted_text


# Test the function.
message = "hello world"
result = encrypt_text(message)

print("Original text:", message)
print("Encrypted text:", result)
