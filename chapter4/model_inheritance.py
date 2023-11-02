from fastapi import FastAPI
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self) -> str:
        return f"{self.content[:140]}..."

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int

class Post(PostBase):
    id: int
    nb_views: int = 0

app = FastAPI()

@app.post("/post", status_code=201)
async def create_post(post: PostCreate):
    return {"post": post}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("model_inheritance:app", host="0.0.0.0", port=5000, reload=True)