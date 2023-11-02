from fastapi import FastAPI, Depends, Header, HTTPException, status

def secret_header(secret_header: str | None = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status_code=403)


app = FastAPI(dependencies=[Depends(secret_header)])
    
@app.get("/route1")
async def route1():
    return{"route": "route1"}

@app.get("/route2")
async def route2():
    return{"route": "route2"}

@app.get("/route3")
async def route3():
    return{"route": "route3"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("global_dependency_1:app", host="0.0.0.0", port=5000, reload=True)