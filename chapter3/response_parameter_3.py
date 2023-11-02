from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str

app = FastAPI()

posts = {
    1: Post(title="Hello"),
}

@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response_parameter_3:app", host="0.0.0.0", port=5000, reload=True)