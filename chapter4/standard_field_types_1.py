from fastapi import FastAPI, status
from pydantic import BaseModel

class Person(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int

app = FastAPI()

@app.post("/person", status_code=status.HTTP_201_CREATED)
async def create_person(person: Person):
    return {"person": person}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("standard_field_types_1:app", host="0.0.0.0", port=5000, reload=True)