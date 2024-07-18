import os
import jwt
from fastapi import HTTPException
from src.config import settings

# Retrieve the secret key and algorithm from environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def get_token_from_request(request):
    # Retrieve the Authorization header from the request
    authorization: str = request.headers.get("Authorization")
    # Check if the Authorization header is missing
    if not authorization:
        # Raise an HTTPException with status code 401 if the Authorization header is missing
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    # Split the Authorization header value to extract the token
    scheme, token = authorization.split()
    # Check if the Authorization header has the Bearer scheme
    if scheme.lower() != "bearer":
        # Raise an HTTPException with status code 401 if the scheme is not Bearer
        raise HTTPException(status_code=401, detail="Invalid scheme")
    return token

# Function to verify the access token extracted from the request
def verify_access_token(request):
    # Extract the token from the request
    token = get_token_from_request(request)

    try:
        # Decode and verify the token using the secret key and algorithm
        payload = jwt.decode(token, settings.access_token_secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # Raise an HTTPException with status code 401 if the token has expired
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        # Raise an HTTPException with status code 401 if the token is invalid
        raise HTTPException(status_code=401, detail="Invalid token")