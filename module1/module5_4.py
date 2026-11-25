import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

MODEL_NAME = "gemma3:270m"
SYSTEM_PROMPT = (
    "You are a patient Python tutor. "
    "Explain concepts simply and give short examples."
)


def ask_ollama(user_prompt):
    # Put the system instructions and user question in the request.
    request_data = {
        "model": MODEL_NAME,
        "system": SYSTEM_PROMPT,
        "prompt": user_prompt,
        "stream": False
    }

    encoded_data = json.dumps(request_data).encode("utf-8")

    request = Request(
        "http://localhost:11434/api/generate",
        data=encoded_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("response", "No response received.")

    except HTTPError as error:
        return f"HTTP error: {error.code}"

    except URLError:
        return "Could not connect to Ollama. Check that Ollama is running."


def main():
    question = input("Enter your question: ").strip()

    if not question:
        print("Please enter a question.")
        return

    answer = ask_ollama(question)
    print("\nOllama's answer:")
    print(answer)


if __name__ == "__main__":
    main()


