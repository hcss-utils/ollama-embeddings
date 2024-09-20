import os

import httpx
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from starlette import status

app = FastAPI()

# Hardcoded secret token for authentication
SECRET_TOKEN = os.environ["FASTAPI_TOKEN"]

# OAuth2 scheme for Bearer token in Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_token(token: str = Depends(oauth2_scheme)) -> bool:
    if token != SECRET_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True


@app.post("/api/embeddings")
async def proxy_embeddings(request: Request, token_valid: bool = Depends(verify_token)):
    request_data = await request.json()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:11434/api/embeddings", json=request_data
        )

    return response.json()
