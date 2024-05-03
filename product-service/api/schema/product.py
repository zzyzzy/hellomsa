from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    pno: int

    class Config:
        from_attributes=True








