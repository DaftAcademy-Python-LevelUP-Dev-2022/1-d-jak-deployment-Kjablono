from datetime import date
from typing import List

from fastapi import FastAPI, Response, status

from pydantic import BaseModel

app = FastAPI()


# zadanie 1.1
@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"start": "1970-01-01"}


# zadanie 1.2
@app.get("/method", status_code=status.HTTP_200_OK)
def method_get():
    return {"method": "GET"}


@app.delete("/method", status_code=status.HTTP_200_OK)
def method_delete():
    return {"method": "DELETE"}


@app.put("/method", status_code=status.HTTP_200_OK)
def method_put():
    return {"method": "PUT"}


@app.options("/method", status_code=status.HTTP_200_OK)
def method_options():
    return {"method": "OPTIONS"}


@app.post("/method", status_code=status.HTTP_201_CREATED)
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
        return Response(status_code=status.HTTP_200_OK)
    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)


# Zadanie 1.4

class EventIn(BaseModel):
    date: str
    event: str


class EventResp(BaseModel):
    id: int
    name: str
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
    response = EventResp(id=new_id, name=event_in.event, date=event_in.date, date_added=today)
    events.append(response)
    return response


# Zadanie 1.5

@app.get("/events/{date}", response_model=List[EventResp])
def get_events_by_date(date: str):
    events_from_date: List[EventResp] = []

    for e in events:
        if e.date == date:
            events_from_date.append(e)
    if len(events_from_date) > 0:
        return events_from_date

    return Response(status_code=status.HTTP_404_NOT_FOUND)
