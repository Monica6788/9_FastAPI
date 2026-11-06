"""
    DB 테이블과 1:1로 대응되는 ORM 모델 모음

    'DB용' 모델만 정의함.
    요청/응답 전용 모델은 schemas.py에서 정의함. (역할 분리)
"""
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Todo(Base):
    """
        todos 테이블
    """
    __tablename__ = "todos"
    # id: int의 int는 파이썬이 관리하도록 하기 위함
    #   => Mapped로 감싸서 DB가 인식할 수 있게 한다.
    id: Mapped[int] = mapped_column(primary_key=True)   # PK
    title:Mapped[str]       # Not Null 지정
    done: Mapped[bool] = mapped_column(default=False)   # 기본값 지정