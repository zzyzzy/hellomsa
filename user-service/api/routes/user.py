from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.services import auth
from api.schema import user as pym
from api.models import user as sqlm

router = APIRouter()

@router.get("/")
async def index():
    return {"message": "Hello World"}


@router.get("/users", response_model=list[pym.User])
async def list_users(db: Session = Depends(get_db)):
    users = db.query(sqlm.User).all()

    return [pym.User.from_orm(u) for u in users]


@router.post("/users", response_model=pym.User)
async def create_user(user: pym.UserCreate, db: Session = Depends(get_db)):
    return auth.register(db, user)


@router.post("/login", response_model=pym.Token)
async def login_user(user: pym.UserLogin, db: Session = Depends(get_db)):
    token = auth.authenticate(db, user)

    if not token:
        raise HTTPException(status_code=401,
                            detail='로그인 실패!! - 아이디나 비밀번호가 틀려요!')

    return token