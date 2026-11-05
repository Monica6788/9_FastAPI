# fastapi-basics
> FastAPI 기본 문법 연습용 프로젝트

## 가상 환경 준비
```bash
python -m venv .venv        # 가상환경 생성

.venv\Scripts\activate      # 가상환경 활성화
.venv\Scripts\deactivate    # 가상환경 비활성화
```
> 💡 **가상환경은 왜 써야 하나요?**
>
> 1. 패키지 충돌(버전) 방지: 컴퓨터 전역에는 패키지 버전을 여러 개씩 설치할 수 없다. 프로젝트별로 필요한 패키지의 버전이 다른데, 하나 실행할 때마다 필요한 버전을 다시 설치하는 것은 비효율적이다.
>
> 2. 시스템 파이썬 보호: 운영체제나 내부 프로그램들이 기본 파이썬 환경을 의존해 작동하는 경우가 생길 수 있다. 또한 전역 환경에 패키지를 마구 설치하거나 지우면 시스템 전체에 문제가 생길 수 있다. 가상환경을 쓰면 내 PC의 핵심 시스템을 건드릴 걱정 없이 안전하게 개발이 가능하다.
>
> 3. 재현 가능성 및 협업 용이성: `pip freeze > requirements.txt`으로 프로젝트에 필요한 패키지를 기록하면 배포할 때 똑같은 환경을 쉽게 재현할 수 있다.

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