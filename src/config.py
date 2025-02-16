import yaml
from pydantic import BaseModel
from yaml.loader import SafeLoader


def get_config(config_path: str):
    # Open the file and load the file
    with open(config_path, encoding='utf-8') as f:
        data = yaml.load(f, Loader=SafeLoader)
        return IConfig(**data)


class LanguageModel(BaseModel):
    model: str
    temperature: float
    ans_max_length: int
    max_tokens: int


class IConfig(BaseModel):
    """
    Base config class
    """
    language_model: LanguageModel


config = get_config('config.yaml')
