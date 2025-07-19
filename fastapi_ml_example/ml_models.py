import asyncio
import concurrent.futures
import math
import random
import time
from typing import Protocol

from fastapi_ml_example.schemes import PredictRequest

WORK_TIME = 1
USE_IMITATION_OF_WORK = False


class MLModel(Protocol):
    def predict(self, batch: list[dict[str, float]]) -> list[float]: ...


def imitation_of_work():
    start = time.time()
    result = 0
    while time.time() - start < WORK_TIME:
        for ind in range(1, 1_000_000):  # ~0.1s
            result += math.sqrt(ind)
    return result


class ExampleMLModel:
    def __init__(self, use_imitation_of_work: bool):
        self.use_imitation_of_work = use_imitation_of_work

    def predict(self, batch: list[dict[str, float]]) -> list[float]:
        if self.use_imitation_of_work:
            imitation_of_work()
        return [random.uniform(0, 1) for _ in range(len(batch))]


_model: MLModel | None = None


def get_model() -> MLModel:
    global _model
    if _model is None:
        _model = ExampleMLModel(USE_IMITATION_OF_WORK)  # load model in memory
    return _model


def _predict(request: PredictRequest) -> list[float]:
    model = get_model()
    return model.predict(request.batch)


async def predict(request: PredictRequest, executor: concurrent.futures.Executor) -> list[float]:
    event_loop = asyncio.get_event_loop()
    return await event_loop.run_in_executor(executor, _predict, request)
