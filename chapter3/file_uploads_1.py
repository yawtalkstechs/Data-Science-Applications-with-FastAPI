from fastapi import FastAPI, File
import uvicorn

app = FastAPI()

@app.post("/files")
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}

if __name__ == "__main__":
    uvicorn.run("file_uploads_1:app", host="0.0.0.0", port=5000, reload=True)