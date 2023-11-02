from fastapi import FastAPI, Depends, Query

app = FastAPI()

async def pagination(skip: int= Query(0, ge=0), limit: int = Query(10, ge=0)) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

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
    uvicorn.run("function_dependency_2:app", host="0.0.0.0", port=5000, reload=True)