import concurrent.futures

import fastapi

from fastapi_ml_example import dependencies, ml_models, schemes

router = fastapi.APIRouter()


@router.post(
    "/predict",
    operation_id="predict",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=schemes.PredictResponse,
    response_class=fastapi.responses.ORJSONResponse,
)
async def predict(
    body: schemes.PredictRequest,
    executor: concurrent.futures.Executor = fastapi.Depends(dependencies.get_executor),
):
    scores = await ml_models.predict(body, executor)
    return fastapi.responses.ORJSONResponse({"scores": scores})
