from typing import Optional

import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    """All service settings"""

    project_name: str = pydantic.Field(
        "fastapi-ml-example", validation_alias="PROJECT_NAME"
    )
    version: str = pydantic.Field("latest", validation_alias="VERSION")
    debug: bool = pydantic.Field(False, validation_alias="DEBUG")

    process_pool_executor_size: int = pydantic.Field(
        8, validation_alias="PROCESS_POOL_EXECUTOR_SIZE"
    )


def get_settings(settings: Optional[Settings] = None, **kwargs) -> Settings:
    if settings:
        assert isinstance(settings, Settings)
        return settings
    return Settings(**kwargs)
