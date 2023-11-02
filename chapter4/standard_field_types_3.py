from fastapi import FastAPI,status
from pydantic import BaseModel
from enum import Enum
from datetime import date

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address

app = FastAPI()

@app.post("/person", status_code=status.HTTP_201_CREATED)
async def create_person(person: Person):
    return {"person": person}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("standard_field_types_3:app", host="0.0.0.0", port=5000, reload=True)