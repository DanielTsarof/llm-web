from llm.requester import get_requester
from config import config

llm_client = get_requester(config.language_model.model)

async def llm_request(message: str):
    pass
