from enum import Enum
from fastapi import FastAPI
import uvicorn

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

if __name__ == "__main__":
    uvicorn.run("path_parameters_3:app", host="0.0.0.0", port=5000, reload=True)