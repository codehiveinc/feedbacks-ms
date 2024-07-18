from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from typing import Annotated
from src.config import settings
from src.shared.domain.entities.base_response_entity import BaseResponseEntity
from src.auth.infrastructure.security.bearer_auth import BearerAuth

oauth2_scheme = BearerAuth(tokenUrl='token')
ALGORITHM = "HS256"


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, settings.access_token_secret, algorithms=[ALGORITHM])
        username: str = payload.get("email")
        if username is None:
            raise JWTError
    except JWTError:
        response = BaseResponseEntity(
            data=None,
            success=False,
            message="Could not validate credentials",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=response.dict(),
        )
    return username
