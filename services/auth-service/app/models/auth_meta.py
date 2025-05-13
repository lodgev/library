from sqlalchemy import Column, String, DateTime, ForeignKey
from app.database import Base
import uuid
from datetime import datetime

class AuthMeta(Base):
    __tablename__ = "auth_meta"

    user_id = Column(String, ForeignKey("auth_users.id", ondelete="CASCADE"), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
    last_sign_in_at = Column(DateTime, nullable=True)
    reset_token = Column(String, nullable=True)
    reset_token_expiration = Column(DateTime, nullable=True)
