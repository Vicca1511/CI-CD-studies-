from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from no where"}


@app.get("/")
async def root():
    return {"message": "Branch de construção paralela! "}    