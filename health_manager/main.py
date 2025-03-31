"""Rest server starts from this file.
All routes are bridged here.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from database import init_db
from schemas import AppInfo
from dependencies import get_app_info
from log import get_logger
import user.routes


log = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Function for lifecycle management in fast api.
    It does following:
        - Defines db initialization before rest server initialization.
    """
    # DB initialization
    init_db()
    yield
    # Server closure activities below
    pass

app = FastAPI(
    title="Rest API for health manager",
    version=get_app_info().app_version,
    lifespan=lifespan)

"""Global Dependencies"""
# Getting application information
app_info: AppInfo = Depends(get_app_info)


@app.get("/")
def root(app_info: AppInfo = app_info):
    """Root endpoint of the rest server"""
    log.debug("Handling root request")
    return {
        "message": f"Welcome to {app_info.app_name}, version:{app_info.app_version}, env:{app_info.app_env}"
        }


# Including routes
app.include_router(user.routes.router)
