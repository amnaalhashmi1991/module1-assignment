import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store the most recently added person while the server is running.
saved_person = None


class Person(BaseModel):
    # The person's name and phone number.
    name: str
    phone_number: str


@app.post("/person")
def add_person(person: Person):
    global saved_person

    # Save the person's information.
    saved_person = {
        "name": person.name,
        "phone_number": person.phone_number
    }

    return {
        "message": "Person saved",
        "person": saved_person
    }


@app.get("/person")
def read_person():
    # Return an error if no person has been saved yet.
    if saved_person is None:
        raise HTTPException(
            status_code=404,
            detail="No person has been saved yet"
        )

    # Add a random number to the saved person's information.
    result = saved_person.copy()
    result["random_number"] = random.randint(1, 100)

    return result
{
  "name": "Amna",
  "phone_number": "0501234567"
}

