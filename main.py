from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


class Post(BaseModel):
    """Post."""

    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorites foods", "content": "i like pizza", "id": 2},
]


@app.get("/")
def get_users():
    """root."""
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    """show all posts"""
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    """create post"""
    return {"post": f"title: {post.title}, content: {post.content}"}
