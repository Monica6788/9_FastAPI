"""저장된 모델 로드 및 추론."""
import joblib
import numpy as np

from app.config import MODEL_PATH
from app.schemas import IrisInput, IrisOutput

_artifact = joblib.load(MODEL_PATH)
_model = _artifact["model"]
_target_names = _artifact["target_names"]


def predict(x: IrisInput) -> IrisOutput:
    features = np.array(
        [[x.sepal_length, x.sepal_width, x.petal_length, x.petal_width]]
    )
    proba = _model.predict_proba(features)[0]
    idx = int(proba.argmax())
    return IrisOutput(
        label=_target_names[idx],
        probability=float(proba[idx]),
        probabilities={n: float(p) for n, p in zip(_target_names, proba)},
    )
