from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.db.session import get_db
from app.models.user import User
from app.core.security import verify_password, get_password_hash, create_access_token
from app.schemas.auth import LoginIn, Token

router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/register", response_model=dict)
def register(payload: LoginIn, db: Session = Depends(get_db)):
    # simple check
    user = db.query(User).filter(User.email == payload.email).first()
    if user:
        raise HTTPException(400, "Email sudah terpakai")

    u = User(
        name=payload.email.split("@")[0],
        email=payload.email,
        password_hash=get_password_hash(payload.password),
        role="admin"
    )
    db.add(u)
    db.commit()
    return {"message": "User registered"}


@router.post("/login", response_model=Token)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(400, "Email atau password salah")

    token = create_access_token(user.email)
    return Token(access_token=token)
