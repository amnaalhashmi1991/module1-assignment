import logging

from fastapi import FastAPI, Request

app = FastAPI()

# Create a logger that writes to both the terminal and my_file.log.
logger = logging.getLogger("request_logger")
logger.setLevel(logging.INFO)
logger.propagate = False

# Add the handlers only once.
if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        "my_file.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Send the request to its route and get the response.
    response = await call_next(request)

    # Log the method, path, and response status.
    logger.info(
        "%s %s %s",
        request.method,
        request.url.path,
        response.status_code
    )

    return response


@app.get("/")
def home():
    # Test route.
    return {"message": "Logging is working"}


@app.get("/hello")
def hello():
    # Another test route.
    return {"message": "Hello"}
