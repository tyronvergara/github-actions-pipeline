"""Main module of a simple API made with FastAPI"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """A typical Hello World message at the root of the API"""
    return {"message": "Hello World"}

@app.get("/status")
async def status():
    """Healthcheck point"""
    return {"status": "OK"}
