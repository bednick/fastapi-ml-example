import pydantic


class PredictRequest(pydantic.BaseModel):
    work_time: int = pydantic.Field(5)


class PredictResponse(pydantic.BaseModel):
    score: float
