from fastapi import APIRouter, Depends

from app.schemas import TodoCreate, TodoOut
from app.database import get_db, Session
from app.models import Todo

# 공통 주소: /todos --> 라우팅 설정(등록)
router = APIRouter(prefix="/todos")
# prefix ---> Spring의 @RequestMapping과 같은 역할

# [GET] /todos/health
# - response: "ok"
# 함수명: health_check
@router.get("/health")
def health_check():
    return "ok"


# [GET]    /todos        할 일 목록 조회 (Read)
@router.get("", response_model=list[TodoOut])
def list_todos(db: Session = Depends(get_db)):
    query = db.query(Todo)

    return query.all()

# [GET]    /todos/{id}   할 일 상세 조회 (Read)
@router.get("/{id}")
def read_detail(id: int):
    return id

# [POST]   /todos        할 일 등록(생성)(Create)
# - request body: {title: "xxx"}
@router.post("")
def create_todo(body: TodoCreate, 
                db: Session = Depends(get_db)):

    todo = Todo(title=body.title)
    db.add(todo)        # 저장할 객체 등록 (DB 처리 전)
    db.commit()         # DML(INSERT)이므로 커밋까지 필수

    db.refresh(todo)    # DB에 적용된 객체를 다시 파이썬으로 읽어옴
    # todo = Todo(title=body.title): 이 단계에서는 id가 없었을 것이다.

    return todo

# [PATCH]  /todos/{id}   할 일 부분 수정 (Update)
@router.patch("/{id}")
def update_todo(id: int):
    return id

# [DELETE] /todos/{id}   할 일 삭제 (Delete)
@router.delete("/{id}")
def delete_todo(id: int):
    return id

