from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes import cats

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(cats.router, prefix="/cats", tags=["cats"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the spy cat agency"}
