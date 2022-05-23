from datetime import date
from typing import List

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


# Zadanie 1.4

class EventIn(BaseModel):
    date: str
    event: str


class EventResp(BaseModel):
    id: int
    event: str
    date: str
    date_added: str


events: List[EventResp] = []


@app.put("/events")
def add_event(event_in: EventIn):
    if len(events) == 0:
        new_id = 0
    else:
        new_id = events[-1].id + 1

    today = date.today().strftime('%Y-%m-%d')
    response = EventResp(id=new_id, event=event_in.event, date=event_in.date, date_added=today)
    events.append(response)
    return response

# Zadanie 1.5
