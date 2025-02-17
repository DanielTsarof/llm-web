import uvicorn

from config import config


def main() -> int:
    uvicorn.run(
        "core.app:get_application",
        factory=True,
        host=config.uvicorn.host,
        port=config.uvicorn.port,
        reload=config.uvicorn.enable_auto_reload,
        log_level=config.uvicorn.log_level,
        workers=config.uvicorn.num_workers,
        root_path=config.uvicorn.root_path,
    )

    return 0
