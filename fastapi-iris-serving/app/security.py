"""Bearer 토큰 인증."""
import secrets

from fastapi import Header, HTTPException

from app.config import API_TOKEN


def verify_token(authorization: str | None = Header(default=None)):
    """Authorization: Bearer <token> 검증."""
    # 토큰을 가지고 있는 사용자의 요청만 받아준다.
    # 토큰 값이 틀리면 요청 처리 안 됨.
    # Bearer: API 인증 시에 사용하는 인증 방식(Scheme)의 이름
    # HTTP 요청을 보낼 때 헤더의 Authorization 필드에 토큰을 담아 보내는데,
    # 이때 이 토큰을 들고(Bearer) 온 사람에게 권한을 부여하겠다는 의미로 앞에 붙인다.
    expected = f"Bearer {API_TOKEN}"
    if authorization is None or not secrets.compare_digest(authorization, expected):
        raise HTTPException(status_code=401, detail="Invalid or missing token")
