from fastapi.security import OAuth2
from fastapi import Request, HTTPException, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowPassword
from typing import Optional
from src.shared.domain.entities.base_response_entity import BaseResponseEntity

class BearerAuth(OAuth2):
    def __init__(self, tokenUrl: str, scheme_name: Optional[str] = None):
        if not tokenUrl:
            raise ValueError("tokenUrl must be provided")
        flows = OAuthFlowsModel(password=OAuthFlowPassword(tokenUrl=tokenUrl))
        super().__init__(flows=flows, scheme_name=scheme_name or self.__class__.__name__)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.headers.get("Authorization")
        if not authorization or not authorization.lower().startswith("bearer "):
            response = BaseResponseEntity(
                data=None,
                success=False,
                message="Not authenticated",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=response.dict(),
                headers={"WWW-Authenticate": "Bearer"},
            )
        return authorization[len("bearer "):]
