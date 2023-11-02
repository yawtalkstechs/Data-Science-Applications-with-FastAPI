from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/picture")
async def get_picture():
    root_directory = Path(__file__).parent.parent
    picture_path = "./cat.jpg"
    return FileResponse(picture_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("custom_response_4:app", host="0.0.0.0", port=5000, reload=True)