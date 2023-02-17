from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from tools import predict, predictModelBenjamin, predictSENET50
import os
import numpy as np


class User_input(BaseModel):
    operation: str
    x: float
    y: float


app = FastAPI()


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.post("/api/upload")
async def create_upload_file(file: UploadFile = File(...)):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())

    json_return = predictSENET50(file_location)

    return {"response code": 200, "message": "Image uploaded successfully!", "result": json_return}
