from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}

if __name__ == "__main__":
    uvicorn.run("query_parameters_3:app", host="0.0.0.0", port=5000, reload=True)