from fastapi import APIRouter, Depends, HTTPException

from app.schemas import TodoCreate, TodoOut, TodoUpdate
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
# 목록 조회는 여러 개이므로 list[Todo]와 같이 list로 한 번 감싼다.
@router.get("", response_model=list[TodoOut])
def list_todos(db: Session = Depends(get_db)):
    query = db.query(Todo)

    return query.all()

# [GET]    /todos/{id}   할 일 상세 조회 (Read)
@router.get("/{id}")
def read_detail(id: int,
                db: Session = Depends(get_db)):
    """ Todo 상세조회 (1건 조회) """

    """
    # 쿼리 객체 생성
    query = db.query(Todo)

    # todolist와 달리 상세 조회는 1건 조회이므로 .one()을 붙여서
    # 해당 데이터 객체를 그대로 반환한다.
    # 조건에 맞는 데이터가 2개 이상이면 MultipleResultsFound 에러 발생
    query.filter(Todo.id == id).one()
    """
    todo = db.get(Todo, id)
    if not todo:
        # 500 오류가 발생하지 않도록 잡아주는 것이 좋다.
        raise HTTPException(status_code=404,
                            detail="Todo Not Found.")
    return todo

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
# TodoUpdate: Pydantic 모델
@router.patch("/{id}", response_model=TodoOut)
def update_todo(id: int, body: TodoUpdate,
                db: Session = Depends(get_db)):
    todo = db.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404,
                            detail="Todo Not Found.")
    # body.model_dump(exclude_unset=True
    # : 요청 시 전달된 데이터만 dict로 만들어 줌
    #  (보내지 않은 데이터는 제외하고 dict로 만듦)
    for key, value in body.model_dump(exclude_unset=True).items():
        # setattr(객체, 속성명, 바꿀값)
        # : 파이썬 내장 함수로, todo 객체의 해당 속성(key) 값을
        #   새로운 값(value)로 변경해준다.
        setattr(todo, key, value)

    db.commit()
    # refresh(todo)
    # : 커밋 직후 DB에 반영된 최신 데이터 상태를 다시 todo 객체로 불러오기
    #   (DB에서 자동 생성된 날짜, ID 등 최신 상태를 동기화 할 때 필수!)
    db.refresh(todo)

    return todo

# [DELETE] /todos/{id}   할 일 삭제 (Delete)
# 204: 성공 후 응답 body가 없을 때, 즉 return이 필요 없음
""" API 명세 일관성(컨벤션) """
# API 통신할 때 어떤 삭제 메서드는 상태코드, 어떤 삭제 메서드는 ID를 돌려주면
# 클라이언트 입장에서 처리하기 어려울 수 있음. 끝단을 맞춰주는 것이 좋다.
@router.delete("/{id}", status_code=204)
def delete_todo(id: int,
                db: Session = Depends(get_db)):
    todo = db.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404,
                            detail="Todo Not Found.")

    # 내부적으로 id값을 가져와서 delete를 실행함
    db.delete(todo)
    # DELETE도 DML이므로 커밋
    db.commit()

    # 응답 코드를 204로 지정했으므로 return은 필요 없어짐.
    # return {"message": "Delete Success.", "id": id}

