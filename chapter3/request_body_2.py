from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_user(user: User):
    return user

if __name__ == "__main__":
    uvicorn.run("request_body_2:app", host="0.0.0.0", port=5000, reload=True)