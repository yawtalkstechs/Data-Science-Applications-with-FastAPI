from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}

if __name__ == "__main__":
    uvicorn.run("query_parameters_1:app", host="0.0.0.0", port=5000, reload=True)