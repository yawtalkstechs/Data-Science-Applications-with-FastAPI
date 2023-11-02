import pytest

from introduction_fixtures import Address, Gender, Person

@pytest.fixture
def address():
    return Address(
        street_address="123 adweso street",
        postal_code= "00233",
        city= "Koforidua",
        country="Ghana",
    )

@pytest.fixture
def person(address):
    return Person(
        first_name = "Alice",
        last_name = "Wayne",
        gender = Gender.FEMALE,
        birthdate = "1995-05-05",
        interests = ["travel", "sports", "hiking"],
        address = address,
    )

def test_address_country(address):
    assert address.country == "Ghana"

def test_person_first_name(person):
    assert person.first_name == "Alice"

def test_person_address_city(person):
    assert person.address.city == "Koforidua"