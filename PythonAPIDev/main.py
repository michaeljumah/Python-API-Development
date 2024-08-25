from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jambo Kenya"}


@app.get("/getuser")
async def get_user():
    return {"message ": "hello"}