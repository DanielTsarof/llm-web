class MessageTooLongError(Exception):
    """Exceptions for case when еhe number of tokens in request exceeds the maximum extended value"""

    description = 'The maximum token limit has been exceeded'

class InvalidModelError(Exception):
    """Exceptions for case when model with this name is not supported."""

    description = 'Invalid model name'
