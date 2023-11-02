from datetime import date
from enum import Enum

from pydantic import BaseModel


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

    def name_dict(self):
        return self.model_dump(include={"first_name", "last_name"})

person = Person(
    first_name="Alice",
    last_name="Wonder",
    gender=Gender.FEMALE,
    birthdate="2000-01-01",
    interests=["travel", "sports", "hiking"],
    address={
        "street_address": "123 Midtown Street",
        "postal_code": "123456",
        "city": "Midtown",
        "country": "UK",
    },
)

name_model = person.model_dump()
print(name_model)