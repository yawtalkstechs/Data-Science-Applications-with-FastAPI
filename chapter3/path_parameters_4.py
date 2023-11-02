from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

@app.get("/users/{id}")
async def get_users(id: int=Path(..., gt=0)):
    return {"user_id": id}

if __name__ == "__main__":
    uvicorn.run("path_parameters_4:app", host="0.0.0.0", port=5000)