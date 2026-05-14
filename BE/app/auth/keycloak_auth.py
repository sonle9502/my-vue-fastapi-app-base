from jose import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

KEYCLOAK_PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuiAvKYUJeBnLeGCcIbjgrmjNCe98rJSqkZhoPiAE3mxilsN/AtWZOEt6VlmYKfl+2vpNvCExg5vFDomPY7onCgebP5glkvhVGWtAY/vd6kk+0DNEZlOHD1mbh1vex8QQBDKhIwtyRUv+VyAQDlqjebcj/fvQEhG+2cx8E/IzIe1pTXXvN3qyUtrIgIDq6BZlCBwohAYpXxTSQTkkKTMHGSkiW/wywD1ovC9HDlNLbQuqKpgw6lTvnPxBy3SzLaqjU7vu/5bkWCB+0KDuhY3ZGG5C+DCB+DY4kKu0se441qRo8NYqP9qhXCDKsA3g+8mqpWKZfmad5U7+TPf86UdSpQIDAQAB
-----END PUBLIC KEY-----
"""

ALGORITHM = "RS256"


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            KEYCLOAK_PUBLIC_KEY,
            algorithms=[ALGORITHM],
            options={"verify_aud": False},
        )

        print(payload)

        return payload

    except Exception as e:

        print("JWT ERROR:", e)

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )