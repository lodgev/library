import uuid
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.auth_user import AuthUser
from app.models.auth_meta import AuthMeta
from app.schemas.auth_user import LoginRequest, RegistrationRequest
from app.services.utils import notify_user, JWT_SECRET, JWT_ALGORITHM


JWT_EXPIRATION_MINUTES = 60


def login_user(db: Session, data: LoginRequest):
    user = db.query(AuthUser).filter(
        (AuthUser.email == data.email_or_username) |
        (AuthUser.username == data.email_or_username)
    ).first()

    if not user or not check_password_hash(user.password, data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Email not verified")

    if user.is_locked:
        raise HTTPException(status_code=403, detail="Account is locked")

    access_token = jwt.encode({
        "user_id": user.id,
        "role": user.role,
        "exp": datetime() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    }, JWT_SECRET, algorithm=JWT_ALGORITHM)

    refresh_token = jwt.encode({
        "user_id": user.id,
        "type": "refresh"
    }, JWT_SECRET, algorithm=JWT_ALGORITHM)

    user.refresh_token = refresh_token
    meta = db.query(AuthMeta).filter(AuthMeta.user_id == user.id).first()
    if meta:
        meta.last_sign_in_at = datetime()
    db.commit()

    return {"access_token": access_token, "refresh_token": refresh_token}


def logout_user(db: Session, user_id: str):
    user = db.query(AuthUser).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.refresh_token = None
    db.commit()
    return {"message": "Successfully logged out"}


def register_user(db: Session, data: RegistrationRequest):
    if db.query(AuthUser).filter((AuthUser.email == data.email) | (AuthUser.username == data.username)).first():
        raise HTTPException(status_code=400, detail="User already exists")

    user = AuthUser(
        id=str(uuid.uuid4()),
        email=data.email,
        username=data.username,
        password=generate_password_hash(data.password),
        role='user',
        is_verified=False,
    )
    db.add(user)
    db.flush()

    meta = AuthMeta(user_id=user.id, created_at=datetime())
    db.add(meta)
    db.commit()

    # Send verification token
    token = str(uuid.uuid4())
    notify_user(
        email=user.email,
        subject="Verify your email",
        message=f"Click the link to verify your account: http://localhost:4444/verify?token={token}"
    )

    return {"message": "User registered, verification email sent."}
