from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response_parameter_1:app", host="0.0.0.0", port=5000, reload=True)