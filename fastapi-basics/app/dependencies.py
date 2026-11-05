"""
    공통으로 사용하는 의존성 모음
"""
from fastapi import Query

def pagination(
        # ge: 최솟값을 0으로 설정 
        skip: int = Query(0, ge=0, description="건너뛸 개수"),
        # le: 최댓값을 100으로 설정
        limit: int = Query(10, ge=1, le=100, description="가져올 개수")
) -> dict:          # 타입 힌트 (반환타입 힌트)
    """
        skip >= 0, 1 <= limit <= 100
        기본값 - skip: 0, default: 10
        ge: 최솟값, le: 최댓값
    """
    return {"skip": skip, "limit": limit}