"""
    Pydantic 모델: 요청/응답 데이터의 모양과 검증 규칙을 정의
"""
from pydantic import BaseModel, Field, ConfigDict
# Field는 정규식 대신 pattern이라는 매개변수를 표준으로 사용한다.

# ItemCreate 클래스: BaseModel 상속
class ItemCreate(BaseModel):
    """
        - name: 1 ~ 50자 문자열
        - age: 0보다 큰 정수 (> 대신 gt)
    """
    name: str = Field(min_length=1, max_length=50)
    price: int = Field(gt=0)

class UserCreate(BaseModel):
    """
        - username
        - password
    """
    username: str
    password: str

# {"id": xx, "username": "xxx"}
class UserOut(BaseModel):
    id: int
    username: str

class TodoCreate(BaseModel):
    title: str = Field(min_length=1)

class TodoOut(BaseModel):
    """
        DB에서 조회한 후, ORM --> 응답
    """
    # ORM 객체의 속성을 읽어서 변환하도록 허용하는 설정
    # 이거 없으면 500 오류
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    done: bool