import functools
import logging

import fastapi.exception_handlers

from fastapi_ml_example import api, config, dependencies


logger = logging.getLogger(__name__)


def get_application(settings: config.Settings) -> fastapi.FastAPI:
    application = fastapi.FastAPI(
        title=settings.project_name,
        debug=settings.debug,
        version=settings.version,
        lifespan=functools.partial(dependencies.lifespan, settings=settings),
    )
    application.include_router(api.router)
    return application
