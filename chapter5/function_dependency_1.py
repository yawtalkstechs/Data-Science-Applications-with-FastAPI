from fastapi import FastAPI, Depends

app = FastAPI()

async def pagination(skip: int= 0, limit: int = 10) -> tuple[int, int]:
    return (skip, limit)

@app.get("/items")
async def list_items(p: tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.get("/things")
async def list_things(p: tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("function_dependency_1:app", host="0.0.0.0", port=5000, reload=True)