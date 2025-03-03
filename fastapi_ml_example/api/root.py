import fastapi

from fastapi_ml_example import config, dependencies

router = fastapi.APIRouter()


@router.get("/", operation_id="root", status_code=fastapi.status.HTTP_200_OK)
def root(settings: config.Settings = fastapi.Depends(dependencies.get_settings)):
    return {"service": settings.project_name, "version": settings.version}
