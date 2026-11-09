"""요청/응답 스키마."""
from pydantic import BaseModel, Field


class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, le=15, description="꽃받침 길이(cm)")
    sepal_width: float = Field(..., gt=0, le=15, description="꽃받침 너비(cm)")
    petal_length: float = Field(..., gt=0, le=15, description="꽃잎 길이(cm)")
    petal_width: float = Field(..., gt=0, le=15, description="꽃잎 너비(cm)")


class IrisOutput(BaseModel):
    label: str
    probability: float
    probabilities: dict[str, float]
