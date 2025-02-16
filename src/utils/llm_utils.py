import tiktoken


def get_prompt(path: str, max_length: int):
    with open(path) as f:
        prompt = f.readlines()
    prompt = prompt[0] + f' Максимальная длина твоего ответа: {max_length} слов.' \
                         f' Вот история диалога: '
    return prompt


def count_tokens(text: str, encoding: str = 'cl100k_base') -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding)
    tokens = encoding.encode(text)
    return len(tokens)
