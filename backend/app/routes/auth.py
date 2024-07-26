import jwt
import secrets
from typing import Annotated
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from core.config import settings
from core import security
from models.auth import TokensResponse, RefreshTokenRequest, User


USERNAME = settings.username
PASSWORD = settings.password

router = APIRouter(prefix='/auth', tags=["Authentication"])

@router.post('/token', response_model=TokensResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not (
        secrets.compare_digest(form_data.username, USERNAME) and
        security.verify_password(form_data.password, PASSWORD)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password", 
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_token(
        {"username": form_data.username},
        timedelta(minutes=settings.access_token_expire_in_minutes)
    )
    
    refresh_token = security.create_token(
        {"username": form_data.username},
        timedelta(days=settings.refresh_token_expire_in_days)
    )
    
    return TokensResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.post('/refresh', response_model=TokensResponse)
def refresh_token(request: RefreshTokenRequest):
    refresh_token = request.refresh_token
    try:
        payload = jwt.decode(refresh_token, settings.secret_key, algorithms=[settings.algorithm])

        username = payload.get("username")
        if not username or not secrets.compare_digest(username, USERNAME):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        access_token = security.create_token(
            {"username": username},
            timedelta(minutes=settings.access_token_expire_in_minutes)
        )

        return TokensResponse(access_token=access_token, refresh_token=refresh_token)

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")


@router.get('/check')
def test(current_user: Annotated[User, Depends(security.get_current_user)]):
    return {"authenticated": "yes"}