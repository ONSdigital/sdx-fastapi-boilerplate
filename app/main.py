from fastapi import FastAPI
import uvicorn

from app.routes import router

app = FastAPI()
app.include_router(router)


def run():
    """
    Run the FastAPI app
    this is a function so it can be called externally
    by poetry etc
    """
    uvicorn.run(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    run()
