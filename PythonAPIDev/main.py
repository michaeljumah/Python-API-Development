from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jambo Kenya"}


@app.get("/getuser")
async def get_user():
    return {"message ": "hello"}


@app.post("/creatposts")
async def create_post(payload: dict= Body(...)):
    print(payload)
    return {"message": "Succsessfully created"}