from fastapi import FastAPI
from typing import Dict
import uvicorn

app = FastAPI()


@app.get("/", response_model=Dict[str, str])
async def hello_world() -> Dict[str, str]:
    return {"message": "hello world"}


if __name__ == '__main__':
    uvicorn.run(app)
