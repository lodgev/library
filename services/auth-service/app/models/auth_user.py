from sqlalchemy import Column, String, Boolean, Integer
from app.database import Base
import uuid

class AuthUser(Base):
    __tablename__ = "auth_users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="guest")  # guest, user, librarian, admin
    is_verified = Column(Boolean, default=False)
    is_locked = Column(Boolean, default=False)
    login_attempts = Column(Integer, default=0)
    refresh_token = Column(String, nullable=True)
    two_fa_enabled = Column(Boolean, default=False)
    two_fa_secret = Column(String, nullable=True)
