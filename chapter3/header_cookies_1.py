from fastapi import FastAPI, Header
import uvicorn

app = FastAPI()

@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}

if __name__ == "__main__":
    uvicorn.run("header_cookies_1:app", host="0.0.0.0", port=5000, reload=True)