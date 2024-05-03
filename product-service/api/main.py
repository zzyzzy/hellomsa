import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import database as sess
from api.routes import product, naver

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000",  # 허용할 프론트엔드 도메인
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router)
app.include_router(naver.router)

if __name__ == '__main__':
    sess.create_tables()
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)


