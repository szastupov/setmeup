import os
from settings import from_environ


def test_enviorment():
    os.environ["DEBUG"] = "1"
    os.environ["PORT"] = "8080"
    os.environ["APP_ENV"] = "production"
    os.environ["ENABLE_HALLUCINATIONS"] = "0"

    @from_environ
    class config:
        DEBUG = False
        PORT = 3000
        APP_ENV = "dev"
        ENABLE_HALLUCINATIONS = True

    assert config.DEBUG is True
    assert config.PORT == 8080
    assert config.APP_ENV == "production"
    assert config.ENABLE_HALLUCINATIONS is False
