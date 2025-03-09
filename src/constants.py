from pathlib import Path

CONFIG_PATH = Path("config.yml")
ENV_PATH = Path(".env")

ENCODINGS = {
    'deepseek-r1': 'cl100k_base',
    'gpt-4': 'cl100k_base',
    'llama3': 'p50k_base'
}
