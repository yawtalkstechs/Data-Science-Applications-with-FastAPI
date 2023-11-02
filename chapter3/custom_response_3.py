from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("custom_response_3:app", host="0.0.0.0", port=5000, reload=True)