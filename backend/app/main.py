from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routes import auth
from core.database import Database
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to the database...")
    database = Database(settings.mongodb_url, settings.mongodb_db)
    yield
    print("Closing the database...")
    database.close()

app = FastAPI(openapi_prefix='/api/v1', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
app.include_router(auth.router)
