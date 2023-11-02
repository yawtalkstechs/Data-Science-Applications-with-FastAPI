from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

app = FastAPI()

posts = {
    1: Post(title="Hello_world", nb_views=100),
}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    posts.pop(id, None)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("response_path_parameter_2:app", host="0.0.0.0", port=5000, reload=True)