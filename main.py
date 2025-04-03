from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_items(item: str | None = None, size: int | None = None):
    return {"item": item, "size": size}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}