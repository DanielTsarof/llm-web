from typing import Literal

import yaml
from dotenv import dotenv_values
from pydantic import BaseModel
from yaml.loader import SafeLoader

from constants import CONFIG_PATH, ENV_PATH

_env = dotenv_values(ENV_PATH.as_posix())


def get_config(config_path: str):
    # Open the file and load the file
    with open(config_path, encoding='utf-8') as f:
        data = yaml.load(f, Loader=SafeLoader)
        return IConfig(**data)


class UvicornConfig(BaseModel):
    host: str = _env["APP_URL"] or "127.0.0.1"
    port: int = int(_env["APP_PORT"] or 5000)
    enable_auto_reload: bool
    log_level: Literal["critical", "error", "warning", "info", "debug", "trace"]
    num_workers: int
    root_path: str


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


config = get_config(CONFIG_PATH)
