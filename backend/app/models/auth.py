from pydantic import BaseModel, Field


class TokensResponse(BaseModel):
    access_token: str = Field()
    refresh_token: str = Field()
    

class RefreshTokenRequest(BaseModel):
    refresh_token: str
    
    
class User(BaseModel):
    username: str