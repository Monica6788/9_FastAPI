"""붓꽃 분류 모델 서빙용 FastAPI 앱."""
from fastapi import Depends, FastAPI

from app.ml import predictor
from app.schemas import IrisInput, IrisOutput
from app.security import verify_token

app = FastAPI(title="Iris Classifier API")


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO: POST /predict 엔드포인트를 직접 작성해 보세요.
# 1. 데코레이터: POST 방식, 경로는 "/predict"로 등록한다.
#    - 응답 스키마: response_model=IrisOutput
#    - 토큰 인증: dependencies=[Depends(verify_token)]
# 2. 함수: 요청 본문을 IrisInput 타입으로 받는다.
# 3. 본문: predictor.predict()에 입력을 전달하고, 결과를 반환한다.
# 힌트: IrisInput, IrisOutput, Depends, verify_token, predictor는 이미 import 되어 있다.
#       위의 /health 엔드포인트를 참고한다.

@app.post("/predict",
          response_model=IrisOutput,
          dependencies=[Depends(verify_token)])
def predict(body: IrisInput):
    result = predictor.predict(body)

    return result
