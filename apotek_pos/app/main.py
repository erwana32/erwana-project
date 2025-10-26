from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api import auth, users

#Buat table saat startup
Base.metadata.create_all(bind=engine)

#initialize FastAPI app
app = FastAPI(title = "Apotek Erza POS API")

#include router
app.include_router(auth.router)
app.include_router(users.router)

#health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}
