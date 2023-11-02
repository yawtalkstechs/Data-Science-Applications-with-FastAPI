from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/files")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    return [
        {"file_name": file.filename,  "content_type": file.content_type}
        for file in files
    ]

if __name__ == "__main__":
    uvicorn.run("file_uploads_3:app", host="0.0.0.0", port=5000, reload=True)