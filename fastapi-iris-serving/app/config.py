"""환경 설정."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = Path(os.environ.get("MODEL_PATH", BASE_DIR / "app" / "ml" / "artifacts" / "model.joblib"))

# 설정되지 않으면 서버가 시작되지 않도록 함 (KeyError)
API_TOKEN = os.environ["API_TOKEN"]
