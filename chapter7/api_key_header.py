from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_TOKEN = "SECRET_API_TOKEN"

app = FastAPI()

api_key_header = APIKeyHeader(name="Token")

@app.get("/protected-route")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_key_header:app", host="0.0.0.0", port=5000, reload=True)