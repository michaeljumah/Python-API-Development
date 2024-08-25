from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jambo Kenya"}


@app.get("/getuser")
async def get_user():
    return {"message ": "hello"}


@app.post("/creatposts")
async def create_post():
    return {"message": "Succsessfully created"}