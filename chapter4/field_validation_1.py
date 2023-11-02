from fastapi import FastAPI, status
from pydantic import BaseModel, Field, EmailStr, HttpUrl

class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: int | None = Field(None, ge=0, le=120)
    email: EmailStr = Field(...)
    website: HttpUrl

app = FastAPI()

@app.post("/person", status_code=status.HTTP_201_CREATED)
async def create_person(person: Person):
    return {"person": person}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("field_validation_1:app", host="0.0.0.0", port=5000, reload=True)