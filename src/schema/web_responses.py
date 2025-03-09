from typing import Literal, Optional, Sequence, Union
from pathlib import Path
from base64 import b64decode, b64encode

from pydantic import BaseModel, model_serializer


class PingBase(BaseModel):
    ping: Literal["pong"]


class Ping(PingBase):
    ...


class Image(BaseModel):
  value: Union[str, bytes, Path]

  @model_serializer
  def serialize_model(self):
    if isinstance(self.value, (Path, bytes)):
      return b64encode(self.value.read_bytes() if isinstance(self.value, Path) else self.value).decode()

    if isinstance(self.value, str):
      try:
        if Path(self.value).exists():
          return b64encode(Path(self.value).read_bytes()).decode()
      except Exception:
        # Long base64 string can't be wrapped in Path, so try to treat as base64 string
        pass

      # String might be a file path, but might not exist
      if self.value.split('.')[-1] in ('png', 'jpg', 'jpeg', 'webp'):
        raise ValueError(f'File {self.value} does not exist')

      try:
        # Try to decode to check if it's already base64
        b64decode(self.value)
        return self.value
      except Exception:
        raise ValueError('Invalid image data, expected base64 string or path to image file') from Exception


class LLMResponse(BaseModel):
  """
  Chat message.
  """

  role: Literal['user', 'assistant', 'system', 'tool']
  "Assumed role of the message. Response messages has role 'assistant' or 'tool'."

  content: Optional[str] = None
  'Content of the message. Response messages contains message fragments when streaming.'

  images: Optional[Sequence[Image]] = None
  """
  Optional list of image data for multimodal models.

  Valid input types are:

  - `str` or path-like object: path to image file
  - `bytes` or bytes-like object: raw image data

  Valid image formats depend on the model. See the model card for more information.
  """