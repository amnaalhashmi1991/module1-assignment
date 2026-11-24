from math import ceil

from fastapi import FastAPI, Query

app = FastAPI()

# Example list of items.
items = [f"Item {number}" for number in range(1, 21)]


@app.get("/items")
def get_items(
    page: int = Query(default=1, ge=1),
    size: int = Query(default=5, ge=1)
):
    # Calculate which part of the list belongs to this page.
    start = (page - 1) * size
    end = start + size
    page_items = items[start:end]

    # Calculate pagination information.
    total_items = len(items)
    total_pages = ceil(total_items / size)

    return {
        "items": page_items,
        "page": page,
        "size": size,
        "total_items": total_items,
        "total_pages": total_pages
    }

fastapi dev module3_6.py
