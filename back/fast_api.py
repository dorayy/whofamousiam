from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from tools import calculate as calc
import os


class User_input(BaseModel):
    operation: str
    x: float
    y: float


app = FastAPI()


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.post("/api/calculate")
def calculate(user_input: User_input):
    return calc(user_input.operation, user_input.x, user_input.y)


@app.post("/api/upload")
async def create_upload_file(file: UploadFile = File(...)):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())

    return {"info": f"File {file.filename} has been saved"}
