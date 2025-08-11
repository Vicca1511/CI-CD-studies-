from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World from no where"}


@app.get("/paralelo")
async def root():
    return {"message": "Branch de construção paralela! "}    