from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

"""Product model representing a single product in the webshop. """

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: HttpUrl
    quantity: int
    created_at: datetime
    
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: HttpUrl
    quantity: int
    created_at: datetime

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[HttpUrl] = None
    quantity: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        extra = 'forbid'