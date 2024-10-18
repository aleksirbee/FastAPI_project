from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    raiting: Optional[int] = None


my_post = [{"title": "Title of post 1", "content": "Content of post 1", "id": 1},
            {"title": "Favorite foods", "content": "I really like sushi", "id": 2}]


@app.get("/")
def root():
    return {"message": "Hello! Welcome to my API project"}

@app.get("/posts")
def get_posts():
    return {"data": my_post} # Sending in json format

@app.post("/createposts")
def create_posts(primer: Post): # extract all fields from the body and covert into python dict and store it in "primer"
    post_dict = primer.model_dump()
    post_dict['id'] = randrange(0, 100000)
    my_post.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Here is the {id} post!"}