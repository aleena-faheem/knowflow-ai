
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[3]

# Create storage directory if it doesn't exist
STORAGE_DIR = BASE_DIR / "storage"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# SQLite database location
DATABASE_URL = f"sqlite:///{STORAGE_DIR / 'knowflow.db'}"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models
Base = declarative_base()


# Dependency for FastAPI database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
