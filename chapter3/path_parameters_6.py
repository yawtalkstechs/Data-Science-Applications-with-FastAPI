from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., pattern=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}

if __name__ == "__main__":
    uvicorn.run("path_parameters_6:app", host="0.0.0.0", port=5000, reload=True)