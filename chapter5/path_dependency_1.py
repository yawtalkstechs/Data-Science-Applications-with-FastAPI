from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI()

def secret_header(secret_header: str | None = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status_code=403)
    
@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}

@app.get("/route")
async def normal_route():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("path_dependency_1:app", host="0.0.0.0", port=5000, reload=True)