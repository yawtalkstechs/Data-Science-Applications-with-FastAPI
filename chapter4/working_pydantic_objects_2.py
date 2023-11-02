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

person_include = person.model_dump(include={"first_name", "last_name"})
print(person_include)  # {"first_name": "John", "last_name": "Doe"}

person_exclude = person.model_dump(exclude={"birthdate", "interests"})
print(person_exclude)

person_nested_include = person.model_dump(
    include={
        "first_name": ...,
        "last_name": ...,
        "address": {"city", "country"},
    }
)
# {"first_name": "John", "last_name": "Doe", "address": {"city": "Woodtown", "country": "US"}}
print(person_nested_include)
