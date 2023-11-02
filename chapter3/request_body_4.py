from fastapi import FastAPI, Body
from pydantic import BaseModel

import uvicorn

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_user(user:User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}

if __name__ == "__main__":
    uvicorn.run("request_body_4:app", host="0.0.0.0", port=5000, reload=True)