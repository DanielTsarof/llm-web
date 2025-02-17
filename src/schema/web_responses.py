from typing import Literal

from pydantic import BaseModel


class PingBase(BaseModel):
    ping: Literal["pong"]


class Ping(PingBase):
    ...
