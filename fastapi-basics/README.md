# fastapi-basics
> FastAPI 기본 문법 연습용 프로젝트

## 가상 환경 준비
```bash
python -m venv .venv        # 가상환경 생성

.venv\Scripts\activate      # 가상환경 활성화
.venv\Scripts\deactivate    # 가상환경 비활성화
```

## 패키지/모듈 설치
```bash
pip install 모듈명
```

**현재 설치된 항목 파일 저장**
```bash
pip freeze > requirements.txt
```

**`requirements.txt` 파일 기준으로 모듈 설치**
```bash
pip install -r requirements.txt
# pip install -r 파일명
```
> 가상환경 안에서 설치해야 하니 경로 앞에 (.venv) 표시 있는지 확인 필수


> `.ipynb` 파일도 가상환경으로 실행하려면 위의 검색창 아이콘에서 Python 환경을 선택하면 된다.

## FastAPI 서버 실행
> 실행의 시작점이 되는 폴더명을 주로 `app/`, 그 안에 `app/main.py` 이렇게 넣어두는 것이 보통이다. 아닌 경우에는 실제 실행 파일의 경로와 파일명을 작성해야 한다.
```bash
fastapi dev app/main.py
```
**위의 가상환경 및 패키지 설치가 모두 완료된 상태여야 한다.**

## 디렉터리 구조
```
app/            # 소스폴더
    main.py     # 앱 생성(서버 생성), 라우터 등록, CORS 설정, ...
    schemas.py  # Pydantic 모델 (DTO 역할을 하는 모델들)
    routers/    # 라우팅 정보
        ...
        ...
```