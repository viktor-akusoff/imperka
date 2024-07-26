from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from core.config import settings

app = FastAPI(openapi_prefix='/api/v1')
security = HTTPBasic()

@app.get("/test")
def testing():
    return {
        "username": settings.username,
        "password": settings.password,
        "secret_key": settings.secret_key
    }