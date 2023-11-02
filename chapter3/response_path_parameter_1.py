from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str


app = FastAPI()

@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response_path_parameter_1:app", host="0.0.0.0", port=5000, reload=True)