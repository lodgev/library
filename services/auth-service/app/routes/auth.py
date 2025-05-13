from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth_user import LoginRequest, LoginResponse, RegistrationRequest
from app.schemas.password_reset import ForgotPasswordRequest, ResetPasswordRequest
from app.services.auth_service import login_user, logout_user, register_user
from app.services.password_reset import request_password_reset, reset_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, data)


@router.post("/logout")
def logout(user_id: str, db: Session = Depends(get_db)):
    return logout_user(db, user_id)


@router.post("/register")
def register(data: RegistrationRequest, db: Session = Depends(get_db)):
    return register_user(db, data)


@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordRequest, db: Session = Depends(get_db)):
    return request_password_reset(db, data.email)


@router.post("/reset-password")
def reset_password_route(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    return reset_password(db, code=data.code, new_password=data.new_password)
