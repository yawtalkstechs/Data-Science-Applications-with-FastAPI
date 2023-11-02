from fastapi import FastAPI
from project.routers.posts import router as post_router
from project.routers.users import router as user_router

app = FastAPI()

app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(user_router, prefix="/users", tags=["users"])