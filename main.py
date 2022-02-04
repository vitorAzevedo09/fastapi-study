from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.param_functions import Body

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def get_users():
    """root."""
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    """show all posts"""
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(new_post: Post):
    """create post"""
    return {"new_post": f"title: {new_post.title}, content: {new_post.content}"}
