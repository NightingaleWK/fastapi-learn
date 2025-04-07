from fastapi import FastAPI
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")
async def read_items(item: str, size: int):
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