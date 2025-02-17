from fastapi import APIRouter

from schema.web_responses import Ping

router = APIRouter()


@router.get("/")
async def ping() -> Ping:
    """Route to test service availability

    Returns
    -------
    Ping
        Test answer
    """

    return Ping(ping="pong")
