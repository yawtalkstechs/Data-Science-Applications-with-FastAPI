from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: str, id: int):
    return {"type": type, "id": id}
    

if __name__ == "__main__":
    uvicorn.run("path_parameters_2:app", host="0.0.0.0", port=5000, reload=True)