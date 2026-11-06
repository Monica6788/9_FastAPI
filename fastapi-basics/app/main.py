from fastapi import FastAPI
# 현재 경로가 app폴더와 같은 depth에 있으니 현재 파일 기준으로 경로 작성
from app.routers import basics, todos
from app.database import Base, engine

# 테이블 자동 생성 --> 이미 존재하는 경우 스킵됨(패스!)
Base.metadata.create_all(engine)

app = FastAPI()

# 라우터 등록
app.include_router(basics.router)
app.include_router(todos.router)

@app.get("/")
def test_root():
    return {"message": "Hello, FastAPI"}