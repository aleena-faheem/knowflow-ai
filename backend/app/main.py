
from fastapi import FastAPI

from backend.app.database.connection import Base, engine
from backend.app.database import models

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KnowFlow AI",
    description="AI-powered Knowledge Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to KnowFlow AI",
        "status": "running"
    }

from fastapi import FastAPI

from backend.app.database.connection import Base, engine
from backend.app.database import models

from backend.app.api.routes import health, dashboard

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KnowFlow AI",
    description="AI-powered Knowledge Assistant",
    version="1.0.0"
)

# Register API routes
app.include_router(
    health.router,
    prefix="/api",
    tags=["Health"]
)

app.include_router(
    dashboard.router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to KnowFlow AI",
        "status": "running"
    }
