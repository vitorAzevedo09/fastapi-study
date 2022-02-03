from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """root."""
    return {"message": "Hello World"}

