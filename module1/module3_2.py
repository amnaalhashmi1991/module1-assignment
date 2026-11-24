from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageRequest(BaseModel):
    # The message received from the user.
    message: str


@app.post("/echo")
def echo_message(data: MessageRequest):
    # Get the current time in UTC.
    server_time = datetime.now(timezone.utc).isoformat()

    # Return the received message and the server timestamp.
    return {
        "message": data.message,
        "timestamp": server_time
    }
    



