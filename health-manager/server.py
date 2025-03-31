"""File start the uvicorn server
It loads the appropiate settings.
"""
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )
