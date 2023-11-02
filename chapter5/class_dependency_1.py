from fastapi import FastAPI, Query,Depends

app = FastAPI()

class Pagination:
    def __init__(self, maximum_limit: int= 100):
        self.maximum_limit = maximum_limit

    async def __call__(self, skip: int = Query(0, ge=0), limit: int = Query(10, ge=0),) -> tuple[int, int]:
        capped_limit = min(self.maximum_limit, limit)
        return (skip, capped_limit)

pagination = Pagination(maximum_limit=150)

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
    uvicorn.run("class_dependency_1:app", host="0.0.0.0", port=5000, reload=True)