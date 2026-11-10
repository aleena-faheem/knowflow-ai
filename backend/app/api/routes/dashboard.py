
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.app.database.connection import get_db
from backend.app.database.models import (
    Document,
    Conversation,
    Message
)

router = APIRouter()


@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):

    # Count total uploaded documents
    total_documents = db.query(Document).count()

    # Count total conversations
    total_conversations = db.query(Conversation).count()

    # Count total messages
    total_messages = db.query(Message).count()

    # Calculate total processed chunks
    processed_chunks = (
        db.query(func.sum(Document.chunk_count)).scalar() or 0
    )

    return {
        "total_documents": total_documents,
        "processed_chunks": processed_chunks,
        "total_conversations": total_conversations,
        "total_messages": total_messages
    }
