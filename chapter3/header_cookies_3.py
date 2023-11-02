from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/")
async def get_cookie(hello:str | None = Cookie(None)):
    return {"hello": hello}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("header_cookies_3:app", host="0.0.0.0", port=5000, reload=True)