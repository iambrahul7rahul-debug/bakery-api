from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    category: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
