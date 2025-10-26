
"""from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserOut
from app.api.deps import require_roles

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserOut], dependencies=[Depends(require_roles("admin"))])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.id.asc()).all()
"""

from fastapi import APIRouter, Depends
from app.api.deps import require_roles, get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def me(user = Depends(get_current_user)):
    return user

@router.get("/", dependencies=[Depends(require_roles("admin"))])
def list_users():
    return {"message": "only admin can see this"}
