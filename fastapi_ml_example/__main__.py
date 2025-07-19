import logging

import uvicorn

from fastapi_ml_example import application, config

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    settings = config.get_settings()
    app = application.get_application(settings)
    uvicorn.run(app, host="127.0.0.1", port=8080, access_log=True)
