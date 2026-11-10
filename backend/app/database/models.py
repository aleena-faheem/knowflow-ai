
from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship

from backend.app.database.connection import Base


def utc_now():
    return datetime.now(timezone.utc)


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)
    upload_date = Column(DateTime(timezone=True), default=utc_now)
    status = Column(String(50), default="uploaded")
    chunk_count = Column(Integer, default=0)


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), default="New Conversation")
    created_at = Column(DateTime(timezone=True), default=utc_now)

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
        nullable=False
    )
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now)

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )
