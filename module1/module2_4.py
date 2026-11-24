import json
import random


class Person:
    def __init__(self, name, number, location, job_title):
        # Store the person's information.
        self.name = name
        self.number = number
        self.location = location
        self.job_title = job_title

    def to_dictionary(self):
        # Convert the person object to a dictionary.
        return {
            "name": self.name,
            "number": self.number,
            "location": self.location,
            "job_title": self.job_title
        }


def create_random_people():
    names = ["Alex", "Sam", "Jordan", "Taylor", "Casey"]
    locations = ["New York", "Chicago", "Seattle", "Miami", "Denver"]
    jobs = ["Teacher", "Engineer", "Designer", "Doctor", "Chef"]

    people = []

    # Create five people with random details.
    for name in names:
        number = f"05{random.randint(0, 99999999):08d}"
        location = random.choice(locations)
        job_title = random.choice(jobs)

        person = Person(name, number, location, job_title)
        people.append(person)

    return people


def save_people_to_json():
    people = create_random_people()

    # Convert the people objects to dictionaries.
    people_data = [person.to_dictionary() for person in people]

    # Save the data in a JSON file.
    with open("people.json", "w", encoding="utf-8") as file:
        json.dump(people_data, file, indent=4)

    print("Five people were saved to people.json")


# Run the program.
save_people_to_json()

