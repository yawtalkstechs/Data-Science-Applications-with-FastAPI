from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"Hello": "World!"}

if __name__ == "__main__":
    uvicorn.run("first_endpoint_1:app", host="0.0.0.0", port=5000, reload=True)