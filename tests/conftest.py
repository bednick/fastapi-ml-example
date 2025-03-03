from typing import Generator

import fastapi.testclient
import pytest

from fastapi_ml_example import application, config, database


@pytest.fixture(scope="package", autouse=True)
def settings() -> config.Settings:
    return config.Settings(
        database=database.config.Settings(
            database_name="fastapi-ml-example-tests",
            pool_size=-1,
        ),
    )


@pytest.fixture(scope="package")
def app(settings: config.Settings) -> fastapi.FastAPI:
    app = application.get_application(settings)
    app.dependency_overrides = {}

    return app


@pytest.fixture()
def client(
    app: fastapi.FastAPI,
) -> Generator[fastapi.testclient.TestClient, None, None]:
    with fastapi.testclient.TestClient(app) as client:
        yield client
