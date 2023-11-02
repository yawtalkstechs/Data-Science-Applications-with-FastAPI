from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.post("/user")
async def create_user(name:str=Form(...), age:int=Form(...)):
    return {"name": name , "age": age}


if __name__ == "__main__":
    uvicorn.run("form_data_1:app", host="0.0.0.0", port=5000, reload=True)