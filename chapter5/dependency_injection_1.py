from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")

async def get_header(user_agent:str = Header(...)):
    return {"user_agent": user_agent}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("dependency_injection_1:app", host="0.0.0.0", port=5000, reload=True)