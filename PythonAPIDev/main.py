from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel 


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
        


@app.get("/")
async def root():
    return {"message": "Jambo Kenya"}


@app.get("/getuser")
async def get_user():
    user = "Denver"
    return {"message ": f"hello {user}"}


@app.post("/creatposts")
async def create_post(new_post: Post):
    print(new_post)
    return {"data": "new_post"}