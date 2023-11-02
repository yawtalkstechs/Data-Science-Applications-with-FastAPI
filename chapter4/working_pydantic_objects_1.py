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
    date_of_birth: date 
    interests: list[str]
    address: Address

person = Person(
    first_name="Alice",
    last_name="Wonder",
    gender=Gender.FEMALE,
    date_of_birth="2000-01-01",
    interests=["travel", "sports", "hiking"],
    address={
        "street_address": "123 Midtown Street",
        "postal_code": "123456",
        "city": "Midtown",
        "country": "UK",
    },
)

person_dict = person.model_dump()
print(person_dict["first_name"])  # "Alice"
print(person_dict["address"]["street_address"])  # "12 Midtown Street"
