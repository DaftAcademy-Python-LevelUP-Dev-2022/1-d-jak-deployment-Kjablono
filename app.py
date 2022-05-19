from typing import Dict

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


# zadanie 1.1
@app.get("/", status_code=200)
def root():
    return {"start": "1970-01-01"}


# zadanie 1.2
@app.get("/method", status_code=200)
def method_get():
    return {"method": "GET"}


@app.delete("/method", status_code=200)
def method_delete():
    return {"method": "DELETE"}


@app.put("/method", status_code=200)
def method_put():
    return {"method": "PUT"}


@app.options("/method", status_code=200)
def method_options():
    return {"method": "OPTIONS"}


@app.post("/method", status_code=201)
def method_post():
    return {"method": "POST"}
