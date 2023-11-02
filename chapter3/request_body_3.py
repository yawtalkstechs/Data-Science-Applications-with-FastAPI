from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str


import uvicorn

app = FastAPI()

@app.post("/user")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}

if __name__ == "__main__":
    uvicorn.run("request_body_3:app", host="0.0.0.0", port=5000, reload=True)