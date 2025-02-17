from typing import Dict, List

import tiktoken
from ollama import AsyncClient

from config import config
from schema.constants import ENCODINGS
from schema.exceptions import MessageTooLongError, InvalidModelError
from schema.llm_requester_base import LLMClientBase, Messages


class LLMClientDeepseek(LLMClientBase):
    def __init__(self, model: str):
        self.model = model
        self.client = AsyncClient()
        self.encoding = tiktoken.get_encoding(ENCODINGS.get(self.model))
        if self.encoding is None:
            raise InvalidModelError(self.model)

    def count_tokens(self, text):
        tokens = self.encoding.encode(text)
        num_tokens = len(tokens)
        return num_tokens

    def count_messages_tokens(self, messages: Messages):
        total_tokens: int = 0
        for message in messages:
            total_tokens += self.count_tokens(message['content'])
        return total_tokens

    async def chat(self, messages: Messages, max_length: int):
        if self.count_messages_tokens(messages) > config.language_model.max_tokens:
            raise MessageTooLongError()
        response = await self.client.chat(model=self.model, messages=messages)
        return response


def get_requester(model: str) -> LLMClientBase:
    if 'deepseek-r1' in model:
        return LLMClientDeepseek(model)
    else:
        raise InvalidModelError(model)
