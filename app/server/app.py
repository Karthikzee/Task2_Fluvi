from fastapi import FastAPI
from server.database import init_db
from server.routes.user import router as Router


app = FastAPI()

app.include_router(Router, tags=["User"], prefix="/user")  # routing user related api calls

@app.on_event("startup")
async def start_db():  # establishing db connection on app start
    await init_db()
