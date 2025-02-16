from abc import ABC, abstractmethod


class LLMClientBase(ABC):

    @abstractmethod
    def count_tokens(self, text) -> int:
        pass

    @abstractmethod
    async def chat(self, message: str, max_length: int):
        pass
