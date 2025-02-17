from fastapi import FastAPI

from api.v1.api import api_router


def get_application() -> FastAPI:
    """FastAPI application factory

    Returns
    -------
    app : FastAPI
        FastAPI application instance
    """

    app = FastAPI()
    app.include_router(api_router)

    return app
