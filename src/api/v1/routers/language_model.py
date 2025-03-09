from fastapi import APIRouter
from fastapi.responses import JSONResponse

from llm.model_api import llm_request
from schema.exceptions import MessageTooLongError
from schema.llm_requester_base import Messages
from schema.web_responses import LLMResponse

llm_router = APIRouter()


@llm_router.post('/completions')
async def post_completions_handler(messages: Messages):
    try:
        response = await llm_request(messages)
        response = LLMResponse(
            role=response.message.role,
            content=response.message.content,
            images=response.message.images
            )
        return JSONResponse(response.model_dump_json(), status_code=200)
    except MessageTooLongError:
        return JSONResponse(
            content='The limit of tokens in messages has been exceeded',
            status_code=400
        )
