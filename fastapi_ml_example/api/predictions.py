import concurrent.futures

import fastapi

from fastapi_ml_example import schemes, dependencies
from fastapi_ml_example import ml_models

router = fastapi.APIRouter()


@router.post(
    "/predict",
    operation_id="predict",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=schemes.PredictResponse,
)
async def predict(
    body: schemes.PredictRequest,
    executor: concurrent.futures.Executor = fastapi.Depends(dependencies.get_executor),
) -> schemes.PredictResponse:
    score = await ml_models.predict(body, executor)
    return schemes.PredictResponse(score=score)
