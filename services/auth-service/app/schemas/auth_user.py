from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional

class LoginRequest(BaseModel):
    email_or_username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None

class RegistrationRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str

class RegistrationResponse(BaseModel):
    message: str

class UserInfoResponse(BaseModel):
    id: str
    email: EmailStr
    username: str
    role: Literal['guest', 'user', 'librarian', 'admin']
    is_verified: bool
