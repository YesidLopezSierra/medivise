from dotenv import load_dotenv
from fastapi import FastAPI

from medivise.routers import (interactions_router, medications_router,
                              user_router)

load_dotenv()


app = FastAPI()


@app.get("/health")
def read_health():
    return {"status": "ok"}


app.include_router(user_router.router)
app.include_router(medications_router.router)
app.include_router(interactions_router.router)
