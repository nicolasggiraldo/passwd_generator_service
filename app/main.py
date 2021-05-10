import uvicorn
from fastapi import FastAPI

from app.responses.password_generator import password_generator

app = FastAPI()


@app.get("/health-check")
def health_check():
    return {"status": "Up and running"}


@app.get("/password-generator")
async def pass_generator(length: int = 10):
    return {"password": password_generator(length=length)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
