from fastapi import FastAPI, Body, HTTPException

app = FastAPI()

@app.post("/password")
async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(status_code=401, detail="Password don't match.")
    return {"message": "Password match."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("raise_errors_1:app", host="0.0.0.0", port=5000, reload=True)