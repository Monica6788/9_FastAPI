from fastapi import APIRouter

# 공통 주소: /todos --> 라우팅 설정(등록)
router = APIRouter(prefix="/todos")
# prefix ---> Spring의 @RequestMapping과 같은 역할

# [GET] /todos/health
# - response: "ok"
# 함수명: health_check
@router.get("/health")
def health_check():
    return "ok"