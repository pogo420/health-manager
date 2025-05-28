"""Rest server starts from this file.
All routes are bridged here.
"""
from fastapi import FastAPI, Depends
from health_manager.schemas import AppInfo
from health_manager.dependencies import get_app_info
from health_manager.log import get_logger
from health_manager.database import engine, Base
import health_manager.user.routes

log = get_logger(__name__)

log.debug("Initializing db...")
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rest API for health manager",
    version=get_app_info().app_version)

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
app.include_router(health_manager.user.routes.router)
