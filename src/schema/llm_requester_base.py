from abc import ABC, abstractmethod
from typing import Dict, List

Messages = List[Dict[str, str]]


class LLMClientBase(ABC):

    @abstractmethod
    def count_tokens(self, text) -> int:
        pass

    @abstractmethod
    async def chat(self, messages: Messages, max_length: int):
        pass
