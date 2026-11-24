from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel):
    # Text is required.
    Text: str


@app.post("/check-text")
def check_text(data: TextRequest):
    # Return the text when it is provided.
    return {
        "message": "Text received",
        "Text": data.Text
    }
{"Text": "Hello"}