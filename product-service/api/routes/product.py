from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
import api.models.product as sqlm
import api.schema.product as pym

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World"}


@router.get("/products", response_model=list[pym.Product])
async def list_products(db: Session = Depends(get_db)):
    products = db.query(sqlm.Product).all()

    return [pym.Product.from_orm(p) for p in products]


@router.post("/products", response_model=pym.ProductCreate)
async def create_products(product: pym.ProductCreate,
                          db: Session = Depends(get_db)):
    product = sqlm.Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return pym.ProductCreate.from_orm(product)
