"""File start the uvicorn server
It loads the appropiate settings.
"""
import uvicorn
from health_manager.dependencies import get_api_settings


def run():
    uvicorn.run(
        "main:app",
        reload=get_api_settings().enable_reload
    )


if __name__ == "__main__":
    run()
