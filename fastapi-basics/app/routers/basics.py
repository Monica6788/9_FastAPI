from fastapi import APIRouter, HTTPException, Depends
from app.schemas import ItemCreate, UserCreate, UserOut
from app.dependencies import pagination

# Spring의 Controller 분리와 동일하게 기능별로 분리한다.
router = APIRouter()

# ------------------
# 임시 DB (메모리상으로 처리)
USERS = {1: {"id": 1, "username": "dante", "password": "1234"}}
ITEMS = [{"id": i, "name": f"item-{i}", "price": 1000 * i} for i in range(1, 11)]
# ------------------

@router.get("/type")
def test_type(x: int):
    """
        FastAPI에서는 타입 힌트가 곧 검증 규칙이다.
    """
    return {"x": x, "type": type(x).__name__}

# [GET] /items {item_id}?q=xx&limit=20
# q: 쿼리스트링(쿼리 매개변수) 키값
# 함수명: read_items
@router.get("/items/{item_id}")
def read_items(item_id: int, q: str | None = None, limit: int = 10):
    """
        경로 매개변수: URL 상의 {item_id}. 매개변수 추가 시
                      URL에 들어 있는 변수 이름과 동일한 이름으로 작성.
        쿼리 매개변수: 그 외의 매개변수 (?q=xx&limit=nn)
        -> 기본값을 지정하게 되면 선택 입력(전달), 없으면 필수 입력(전달)
    """
    return {"item_id": item_id, "q": q, "limit": limit}

# [POST] /items
# 함수명: create_item
# status_code=201: 성공 시 응답 코드를 201(Created)로 지정
@router.post("/items", status_code=201)
def create_item(item: ItemCreate):
    """
        요청 Body / Pydantic 검증
        - 매개변수 타입이 BaseModel이면 FastAPI가 JSON Body로 인식
    """
    return item

# [POST] /users
# 함수명: create_user
# request body: {"username": "xxx", "password": "xxx"}
# response: {"username": "xxx", "password": "xxx"}
#       => {"id": nn, "username": "xxx"}
@router.post("/users", status_code=201, response_model=UserOut)
def create_user(user: UserCreate):
    """ 응답 데이터 필터링 (response_model) """
    new_id = max(USERS) + 1    # dict에서 최댓값 찾아서 +1
    USERS[new_id] = {"id": new_id,
                     "username": user.username,
                     "password": user.password}

    # return user
    return USERS[new_id]

# [GET] /users/{user_id}
# - response: {"id": nn, "username": "xxx"}
# 함수명: get_user
@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    """ 데이터가 없을 경우 HTTPException으로 오류 응답 처리 """
    user = USERS.get(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")

    return user

# [GET] /items?skip=n&limit=n
# - response: {"skip": n, "limit": n}
# 함수명: list_items
@router.get("/items")
def list_items(page: dict = Depends(pagination)):
    start = page["skip"]
    return ITEMS[ start: start + page["limit"] ]
