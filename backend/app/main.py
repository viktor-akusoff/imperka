from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.security import oauth2_scheme
from routes import auth
from typing import Annotated

app = FastAPI(openapi_prefix='/api/v1')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
app.include_router(auth.router)
