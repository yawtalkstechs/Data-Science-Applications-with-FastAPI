from fastapi import FastAPI, status, HTTPException, Body

app = FastAPI()

@app.post("/password")
async def check_password(password: str = Body(...), password_again: str = Body(...)):
    if password != password_again:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 
                            detail={"message":"Password does not match",
                                    "hints": "Try to make the password visible by clicking on the eye icon to check your typing."})
    return {"message": "Password match"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("raise_errors_2:app", host="0.0.0.0", port=5000, reload=True)