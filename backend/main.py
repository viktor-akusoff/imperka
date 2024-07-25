from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

USER_CREDENTIALS = {"admin": "password"}

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = credentials.username == list(USER_CREDENTIALS.keys())[0]
    correct_password = credentials.password == list(USER_CREDENTIALS.values())[0]
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

@app.get("/secret")
def secret_resource(authenticated: bool = Depends(authenticate)):
    if authenticated:
        return {"message": "This is a secret resource!"}