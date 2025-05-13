from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from app.database import Base
import uuid

class AuthEmailToken(Base):
    __tablename__ = "auth_email_codes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("auth_users.id", ondelete="CASCADE"))
    code = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
