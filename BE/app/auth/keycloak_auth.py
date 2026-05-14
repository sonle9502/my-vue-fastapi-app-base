from jose import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

KEYCLOAK_PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1oq3otzNJGV5AiV5eWuIIFMqmG53J5MUxsLSFiy+18v0zXPxK3r3fh/up2u1a4gS5GdnmKZbiRCMox95nDHfWbtdIkU1GKiYym0dk/eiu3eiUZ7G4RPV7sU2Xf5zPvlCkof/4ePrOQVqXW1wOxJA00pCOUu9vPU1AvFmbYxng6PDQLyVqN7m4HRDAYYYqNOB99Y1mHKdijeJDBunT73erixWjn2lj7BPEJmiakP1/s2oHYaz+IAWYOGnxAF+fZMK8rlYAaPc6x/uiKkeoLfQa4IE2HouHO0xm4DJ7k5mmTchcREUjP3cN5UDAk3i0vMfx3WKAQT09rVWLwrfeSOgPwIDAQAB
-----END PUBLIC KEY-----
"""

ALGORITHM = "RS256"


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        print(KEYCLOAK_PUBLIC_KEY)
        payload = jwt.decode(
            token,
            KEYCLOAK_PUBLIC_KEY,
            algorithms=[ALGORITHM],
            options={"verify_aud": False},
            issuer="http://localhost:8080/realms/my-app",
            
        )

        print(payload)

        return payload

    except Exception as e:

        print("JWT ERROR:", e)
        
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )