from enum import Enum
from fastapi import FastAPI
import uvicorn

class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()

@app.get("/users")
async def get_user(format: UsersFormat):
    return {"format": format}

if __name__ == "__main__":
    uvicorn.run("query_parameters_2:app", host="0.0.0.0", port=5000, reload=True)