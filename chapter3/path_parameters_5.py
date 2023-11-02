from fastapi import FastAPI,Path
import uvicorn

app = FastAPI()

@app.get("/users/address/{address}")
async def get_user_phone_number(address: str = Path(..., min_length=10)):
    return {"address": address}

if __name__ == "__main__":
    uvicorn.run("path_parameters_5:app", host="0.0.0.0", port=5000, reload=True)