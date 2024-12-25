import asyncio
import time
import math
import random
import concurrent.futures
import pickle
import pathlib

from fastapi_ml_example.schemes import PredictRequest


class ExampleMLModel:
    def predict(self, work_time: float) -> float:
        start = time.time()
        result = 0
        while time.time() - start < work_time:
            for ind in range(1, 10_000_000):
                result += math.sqrt(ind)
        return random.uniform(0, 1)


_model: ExampleMLModel | None = None


def get_model() -> ExampleMLModel:
    global _model
    if _model is None:
        path = pathlib.Path(__file__).parent.parent / "model.pkl"
        if not path.exists():
            raise ValueError("No model.pkl found, use `python ml_model_dump.py`")
        with open(path, "rb") as fp:
            _model = pickle.load(fp)
    return _model


def _predict(request: PredictRequest) -> float:
    model = get_model()
    return model.predict(work_time=request.work_time)


async def predict(
    request: PredictRequest, executor: concurrent.futures.Executor
) -> float:
    event_loop = asyncio.get_event_loop()
    return await event_loop.run_in_executor(executor, _predict, request)
