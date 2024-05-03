import sqlalchemy
from sqlalchemy.orm import sessionmaker
from api.models.product import Base

db_url = 'sqlite:///product.db'

engine = sqlalchemy.create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False,
                    autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(engine)


# 데이터베이스 세션 의존성 생성
# def get_db():
#     db = sess.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
def get_db():
    with SessionLocal() as db:
        yield db
