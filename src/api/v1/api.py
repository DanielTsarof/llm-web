from fastapi import APIRouter

from api.v1.routers import ping, language_model


api_router = APIRouter(prefix='/api/v1')
api_router.include_router(ping.router, prefix='/ping', tags=['test'])
api_router.include_router(language_model.llm_router, prefix='/chat')
