from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header

def secret_header(secret_header: str | None = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status_code=403)

router = APIRouter(dependencies=[Depends(secret_header)])

@router.get("/route1")
async def router_route1():
    return{"route": "route1"}

@router.get("/route2")
async def router_route2():
    return{"route": "route2"}

@router.get("/route3")
async def router_route3():
    return{"route": "route3"}

app = FastAPI()
app.include_router(router, prefix="/router")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("router_dependency_1:app", host="0.0.0.0", port=5000, reload=True)