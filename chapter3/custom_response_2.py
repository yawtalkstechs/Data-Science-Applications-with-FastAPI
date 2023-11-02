from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url")


if __name__ == "__main__":
    uvicorn.run("custom_response_2:app", host="0.0.0.0", port=5000, reload=True)