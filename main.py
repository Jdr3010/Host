from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hi():
    return {"message": "hi everyone"}
