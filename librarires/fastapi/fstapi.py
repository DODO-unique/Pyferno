from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.get("/")
def root():

    return {"name": "Victor"}