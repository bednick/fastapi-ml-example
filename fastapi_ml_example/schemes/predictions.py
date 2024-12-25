import pydantic


class PredictRequest(pydantic.BaseModel):
    work_time: int


class PredictResponse(pydantic.BaseModel):
    score: float
