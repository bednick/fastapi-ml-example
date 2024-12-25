import fastapi

from fastapi_ml_example.api import ping, predictions, root

router = fastapi.APIRouter()

router.include_router(ping.router)
router.include_router(predictions.router)
router.include_router(root.router)
