from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routes import auth, media, pages
from app.core.database import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to the database...")
    yield
    print("Closing the database...")
    db.close()

app = FastAPI(openapi_prefix='/api/v1', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
app.include_router(auth.router)
app.include_router(media.router)
app.include_router(pages.router)
