from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()

@app.post("/users")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}

if __name__ == "__main__":
    uvicorn.run("request_body_1:app", host="0.0.0.0", port=5000, reload=True)