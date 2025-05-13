from datetime import datetime, timedelta
import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.models.auth_user import AuthUser
from app.models.auth_password_reset import AuthPasswordReset
from app.services.utils import notify_user


def request_password_reset(db: Session, email: str):
    user = db.query(AuthUser).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    code = f"{uuid.uuid4()}"
    expires_at = datetime() + timedelta(minutes=15)

    reset = AuthPasswordReset(
        id=str(uuid.uuid4()),
        user_id=user.id,
        code=code,
        expires_at=expires_at
    )
    db.add(reset)
    db.commit()

    notify_user(
        email=user.email,
        subject="Reset your password",
        message=f"Use this code to reset your password: {code}"
    )

    return {"message": "Reset code sent to your email."}


def reset_password(db: Session, code: str, new_password: str):
    token = db.query(AuthPasswordReset).filter_by(code=code, used=False).first()
    if not token or token.expires_at < datetime():
        raise HTTPException(status_code=400, detail="Invalid or expired code")

    user = db.query(AuthUser).filter_by(id=token.user_id).first()
    user.password = generate_password_hash(new_password)

    token.used = True
    db.commit()

    notify_user(
        email=user.email,
        subject="Password changed",
        message="Your password was successfully updated."
    )

    return {"message": "Password updated successfully"}
