from typing import Dict

from fastapi import FastAPI, Response

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


# Zadanie 1.3
@app.get("/day")
def day_validate(*, name: str, number: int):
    valid_days = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }

    if name in valid_days.keys() and valid_days[name] == number:
        return Response(status_code=200)
    else:
        return Response(status_code=400)