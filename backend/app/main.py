from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from core.security import oauth2_scheme
from routes import auth
from typing import Annotated

app = FastAPI(openapi_prefix='/api/v1')
    
app.include_router(auth.router)

@app.get('/test')
def test(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "yes"}