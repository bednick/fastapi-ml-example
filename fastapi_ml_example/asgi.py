from fastapi_ml_example import application, config

settings = config.get_settings()
app = application.get_application(settings)
