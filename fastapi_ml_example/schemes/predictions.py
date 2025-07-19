import pydantic


class PredictRequest(pydantic.BaseModel):
    batch: list[dict[str, float]]


class PredictResponse(pydantic.BaseModel):
    scores: list[float]
