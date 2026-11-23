class PersonAddress:
    def __init__(self, name, contact, address, phone_number):
        # Store the person's information.
        self.name = name
        self.contact = contact
        self.address = address
        self.phone_number = phone_number

    def save_to_file(self):
        # Save the person's information in a text file.
        with open("people.text", "a", encoding="utf-8") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Contact: {self.contact}\n")
            file.write(f"Address: {self.address}\n")
            file.write(f"Phone number: {self.phone_number}\n")
            file.write("--------------------\n")


def run_program():
    # Ask the user to enter the person's information.
    name = input("Enter the person's name: ")
    contact = input("Enter contact information: ")
    address = input("Enter the person's address: ")
    phone_number = input("Enter the phone number: ")

    # Create a person and save the information.
    person = PersonAddress(name, contact, address, phone_number)
    person.save_to_file()

    print("The information was saved in people.text")


# Run the program.
run_program()