from llm.requester import get_requester
from schema.llm_requester_base import Messages
from config import config

llm_client = get_requester(config.language_model.model)

async def llm_request(messages: Messages):
    response = await llm_client.chat(messages, max_length=config.language_model.ans_max_length)
    return response
