from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get_request_object(request:Request):
    return {"request": request.url.path}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("request_object_1:app", host="0.0.0.0", port=5000, reload=True)