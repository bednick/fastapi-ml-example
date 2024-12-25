import asyncio
import concurrent.futures
import math
import random
import time
from typing import Protocol

from fastapi_ml_example.schemes import PredictRequest


class MLModel(Protocol):
    def predict(self, **kwargs) -> float: ...


class ExampleMLModel:
    def predict(self, work_time: float = 5, **kwargs) -> float:
        start = time.time()
        result = 0
        while time.time() - start < work_time:
            for ind in range(1, 10_000_000):
                result += math.sqrt(ind)
        return random.uniform(0, 1)


_model: MLModel | None = None


def get_model() -> MLModel:
    global _model
    if _model is None:
        _model = ExampleMLModel()  # load model in memory
    return _model


def _predict(request: PredictRequest) -> float:
    model = get_model()
    return model.predict(**request.model_dump())


async def predict(request: PredictRequest, executor: concurrent.futures.Executor) -> float:
    event_loop = asyncio.get_event_loop()
    return await event_loop.run_in_executor(executor, _predict, request)
