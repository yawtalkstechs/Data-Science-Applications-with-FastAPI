from fastapi import FastAPI, status
from enum import Enum
from datetime import date
from pydantic import BaseModel

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]

app = FastAPI()

@app.post("/person", status_code=status.HTTP_201_CREATED)
async def create_person(person: Person):
    return {"person": person}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("standard_field_types_2:app", host="0.0.0.0", port=5000, reload=True)
