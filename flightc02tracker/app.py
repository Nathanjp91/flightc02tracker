import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"hello": "test"}

if __name__ == "__main__":
    uvicorn.run(
            "app:app",
            host="127.0.0.1",
            port=5000,
            log_level="info",
            reload=True
        )
