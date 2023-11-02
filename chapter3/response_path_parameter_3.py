from fastapi import FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

app = FastAPI()

posts = {
    1: Post(title="Hello_world", nb_views=100),
}

@app.get("/posts/{id}")
async def create_post(id:int):
    return posts[id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response_path_parameter_3:app", host="0.0.0.0", port=5000, reload=True)