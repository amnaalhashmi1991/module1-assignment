def count_address_words(file_name):
    addresses = []

    # Read the file and collect address lines.
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Address:"):
                address = line.split(":", 1)[1].strip()
                addresses.append(address)

    # Count the words and append the results to the same file.
    with open(file_name, "a", encoding="utf-8") as file:
        for address in addresses:
            word_count = len(address.split())
            file.write(f"Address word count: {word_count}\n")


# Run the function.
count_address_words("people.text")
print("Address word counts were added to people.text.")
