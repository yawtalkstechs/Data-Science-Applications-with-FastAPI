from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response_parameter_2:app", host="0.0.0.0", port=5000, reload=True)