# fastapi-iris-serving

붓꽃(Iris) 품종 분류 모델을 FastAPI로 서빙하는 서버입니다.
`POST /predict`로 꽃받침/꽃잎 길이·너비를 보내면 품종과 확률을 반환합니다.

### 패키지 설치

```bash
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

### 모델 파일

`app/ml/artifacts/model.joblib`이 이미 포함되어 있어 바로 실행할 수 있습니다.
모델을 다시 학습하려면 프로젝트 루트에서 아래를 실행하세요.

```bash
python -m training.train
```

## 실행 방법

프로젝트 루트(`fastapi-iris-serving/`)에서 실행합니다.

```bash
$env:API_TOKEN="원하는-긴-랜덤-문자열"
uvicorn app.main:app --port 8000
```

개발 중 코드 변경을 자동 반영하려면 `--reload`를 추가합니다.

서버가 시작되면 모델을 한 번 메모리에 로드하고, 이후 요청에서 재사용합니다.
모델 파일이 없으면 시작 단계에서 에러가 납니다.

### 환경변수

| 이름 | 필수 | 설명 |
|------|------|------|
| `API_TOKEN` | 필수 | `/predict` 호출 시 필요한 Bearer 토큰 |
| `MODEL_PATH` | 선택 | 모델 파일 경로 (기본값: `app/ml/artifacts/model.joblib`) |

## API

### `GET /health`

인증 없이 서버 상태를 확인합니다.

```bash
curl localhost:8000/health
# {"status":"ok"}
```

### `POST /predict`

`Authorization: Bearer <API_TOKEN>` 헤더가 필요합니다.

| 필드 | 설명 | 허용 범위 |
|------|------|-----------|
| `sepal_length` | 꽃받침 길이(cm) | 0 초과 15 이하 |
| `sepal_width` | 꽃받침 너비(cm) | 0 초과 15 이하 |
| `petal_length` | 꽃잎 길이(cm) | 0 초과 15 이하 |
| `petal_width` | 꽃잎 너비(cm) | 0 초과 15 이하 |

```bash
curl -X POST localhost:8000/predict \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

응답 형식:

```json
{
  "label": "setosa",
  "probability": 0.98,
  "probabilities": {"setosa": 0.98, "versicolor": 0.02, "virginica": 0.0}
}
```

위 예시의 확률 값은 형식을 보여 주기 위한 것이며 실제 값은 다를 수 있습니다.

| 상태 코드 | 의미 |
|-----------|------|
| 401 | 토큰이 없거나 틀림 |
| 422 | 입력값 검증 실패 (누락, 범위 초과 등) |

실행 후 `http://localhost:8000/docs`에서 Swagger UI로도 테스트할 수 있습니다.

## 프로젝트 구조

```
iris-serving/
├── app/
│   ├── main.py       # FastAPI 앱, 라우트
│   ├── schemas.py    # 요청/응답 스키마
│   ├── security.py   # Bearer 토큰 검증
│   ├── config.py     # 설정 (토큰, 모델 경로)
│   └── ml/
│       ├── predictor.py          # 모델 로드와 추론
│       └── artifacts/
│           └── model.joblib      # 학습된 모델
├── training/
│   └── train.py      # 학습 스크립트
├── requirements.txt
└── README.md
```