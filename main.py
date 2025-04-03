from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_items(item: str | None = None, size: int | None = None):
    return {"item": item, "size": size}