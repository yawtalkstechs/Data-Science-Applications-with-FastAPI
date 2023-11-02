from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename, "content_type": file.content_type}

if __name__ == "__main__":
    uvicorn.run("file_uploads_2:app", host="0.0.0.0", port=5000, reload=True)