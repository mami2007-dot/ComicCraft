from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import router


# Create FastAPI application
app = FastAPI(
    title="Comic Craft",
    description="AI-powered comic creation application",
    version="1.0.0"
)


# Serve static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Register application routes
app.include_router(router)