import contextlib
import concurrent.futures
import logging
from typing import AsyncIterator

import fastapi


from fastapi_ml_example import config

logger = logging.getLogger(__name__)

__all__ = ("lifespan", "get_settings", "get_executor")


@contextlib.asynccontextmanager
async def lifespan(
    app: fastapi.FastAPI, settings: config.Settings
) -> AsyncIterator[None]:
    app.state.settings = settings  # type: ignore
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=settings.process_pool_executor_size
    ) as executor:
        app.state.executor = executor  # type: ignore
        yield


def get_settings(request: fastapi.Request) -> config.Settings:
    return request.app.state.settings


def get_executor(request: fastapi.Request) -> concurrent.futures.ProcessPoolExecutor:
    return request.app.state.executor
