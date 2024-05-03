from datetime import timedelta, datetime
from typing import Optional

import bcrypt
import jwt
from sqlalchemy.orm import Session

from api.schema import user as pym
from api.models import user as sqlm

# 비밀번호 해싱을 위한 솔트값
SALT = bcrypt.gensalt()

# 토큰생성시 사용할 비밀키
SECRETKEY = 'Hello, World!!'

# 회원가입 처리
def register(db: Session, user:pym.UserCreate):
    hashed_passwd = (bcrypt.hashpw(user.passwd.encode('utf-8'), SALT))
    print(hashed_passwd)

    user = sqlm.User(**user.model_dump())
    user.passwd = hashed_passwd
    user.regdate = datetime.now().isoformat(' ', 'seconds')
    db.add(user)
    db.commit()
    db.refresh(user)
    return pym.User.from_orm(user)


# 액세스 토큰 생성
# JWT : JSON Web Token
# 웹 어플리케이션에서 정보를 안전하게 전송하기 위해 사용되는 표준 방법
# JWT는 토큰 기반 인증시스템을 구현하는데 사용
# 주로 클라이언트/서버 간 정보 교환에 안전하게 사용할 수 있음
# HS256 : 토큰 생성시 사용할 해시 알고리즘 중 하나
def generate_access_token(
    userid: str, expires_delta: Optional[timedelta] = None):

    # 토큰 유효기간 설정 (기본 30분)
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=30)

    # 토큰 발급
    to_encode = {'sub': userid, 'exp': expire}
    encode_jwt = jwt.encode(to_encode,
            SECRETKEY, algorithm='HS256')

    return encode_jwt


# 로그인 처리
def authenticate(db: Session, user: pym.UserLogin):
    dbuser = db.query(sqlm.User)\
            .filter(sqlm.User.userid == user.userid).first()

    if not dbuser:
        return None

    if not bcrypt.checkpw(
            user.passwd.encode('utf-8'), dbuser.passwd):
        return None

    token = generate_access_token(user.userid)

    #return {'access_token': token, 'token_type': 'bearer'}
    return pym.Token(access_token=token, token_type='bearer')








