"""붓꽃 분류 모델 학습 후 app/ml/artifacts/model.joblib 로 저장.

실행: python -m training.train   (프로젝트 루트에서)
"""
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

MODEL_PATH = Path(__file__).resolve().parent.parent / "app" / "ml" / "artifacts" / "model.joblib"

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(f"accuracy: {accuracy_score(y_test, pred):.3f}")
print(classification_report(y_test, pred, target_names=iris.target_names))

MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
joblib.dump({"model": model, "target_names": list(iris.target_names)}, MODEL_PATH)
print(f"saved: {MODEL_PATH}")
