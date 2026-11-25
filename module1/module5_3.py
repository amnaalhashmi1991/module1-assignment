
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:270m"


def ask_ollama(user_prompt):
    # Prepare the request data for Ollama.
    request_data = {
        "model": MODEL_NAME,
        "prompt": user_prompt,
        "stream": False
    }

    # Convert the data to JSON bytes for the HTTP request.
    encoded_data = json.dumps(request_data).encode("utf-8")

    request = Request(
        OLLAMA_URL,
        data=encoded_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        # Send the request and read Ollama's JSON response.
        with urlopen(request, timeout=120) as response:
            response_data = json.loads(response.read().decode("utf-8"))

        return response_data.get("response", "No response was returned.")

    except HTTPError as error:
        error_details = error.read().decode("utf-8", errors="replace")
        return f"HTTP error {error.code}: {error_details}"

    except URLError as error:
        return (
            "Could not connect to Ollama. Make sure Ollama is running. "
            f"Details: {error.reason}"
        )


def main():
    # Get a question from the user.
    user_prompt = input("Enter your question: ").strip()

    if not user_prompt:
        print("Please enter a question.")
        return

    # Send the question to Ollama and display its answer.
    answer = ask_ollama(user_prompt)
    print("\nOllama's answer:")
    print(answer)


if __name__ == "__main__":
    main()

