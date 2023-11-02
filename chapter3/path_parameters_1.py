from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users/{id}")
async def get_user(id:int):
    return {"id": id}

if __name__ == "__main__":
    uvicorn.run("path_parameters_1:app", host="0.0.0.0", port=5000, reload=True)